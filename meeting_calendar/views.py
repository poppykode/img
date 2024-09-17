import calendar
from django.db.models import Q
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from accounts.forms import SessionExpectationAndAvailabilityInfoForm
from core.decorators import role_required
from core.email import Email
from core.enums import DayEnum, RoleEnum, MeetingStatusEnum
from meeting_calendar.forms import AvaliabilityForm, BookMeetingForm, QuickMeeting
from .utils import Calendar, meetings_due_for_check_in, meetings_due_for_check_out
from .models import BookedMeeting, Avaliability, MeetingCheckInAndOut
from datetime import datetime, timedelta, date
from accounts.models import SessionExpectationAndAvailabilityInfo, User


class CalendarView(generic.ListView):
    model = BookedMeeting
    template_name = "calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        qs = None

        user = self.request.user
        qs = BookedMeeting.objects.filter(
            start_date__year=d.year, start_date__month=d.month, requested=user
        )
        cal = Calendar()
        html_cal = cal.formatmonth(withyear=True, qs=qs, y=d.year, m=d.month)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split("-"))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month
 
def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month
@role_required(
    allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value]
)
def meetings(request):
    template_name = 'meetings.html'
    user = request.user
    incoming_meetings = BookedMeeting.objects.filter(requested = user).filter(accepted = False).exclude(booking_date__lt = date.today()).exclude(cancelled =True).exclude(rejected =True)
    outgoing_meetings = BookedMeeting.objects.filter(requester = user).filter(accepted = False).exclude(booking_date__lt = date.today()).exclude(cancelled =True).exclude(rejected =True)
    upcoming_meetings = BookedMeeting.objects.for_user(user).filter(accepted = True).exclude(booking_date__lt = date.today())
    message_history = BookedMeeting.objects.for_user(user).filter(booking_date__lt = date.today()).exclude(requested = None)
    quick_meetings = BookedMeeting.objects.quick_meetings(user)
    context ={
        'form': QuickMeeting(),
        'incoming_meetings':incoming_meetings,
        'outgoing_meetings':outgoing_meetings,
        'upcoming_meetings':upcoming_meetings,
        'message_history':message_history,
        'quick_meetings':quick_meetings
    }
    return render(request, template_name, context)

@role_required(
    allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value, RoleEnum.COACH.value]
)
def availability(request, user_id=None):
    template_name = "availability.html"
    if not user_id:
        if request.user:
            is_avaliability = Avaliability.objects.filter(user=request.user).exists()
            request.session["has_availabilty"] = is_avaliability
    user = request.user
    qs = Avaliability.objects.filter(user=user).exclude(is_temp=True)
    if user_id:
        user_ = get_object_or_404(User, id=user_id)
        user = user_
        qs = Avaliability.objects.filter(user=user_).exclude(is_temp=True).exclude(is_disabled=True)
    return render(request, template_name, {"avail": qs, "user": user})

@role_required(allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value])
def create_availability(request):
    template_name = "create_availability.html"
    form = AvaliabilityForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            if is_overlapping_availabilities_func(request, form.cleaned_data):
                messages.error(
                    request,
                    "This availability overlaps with an existing one. Please choose a different time slot.",
                )
                return redirect("meeting_calendar:create_availability")

            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Availability successfully added.")
            return redirect("meeting_calendar:availability")

    return render(request, template_name, {"form": form, "type": "create"})

def is_overlapping_availabilities_func(request, data):
    return (
        Avaliability.objects.filter(
            Q(user=request.user)
            & Q(day=data["day"])
            & (
                Q(  # Overlap scenarios:
                    # Existing availability starts before and ends after the new one
                    Q(start_time__lt=data["start_time"])
                    & Q(end_time__gt=data["end_time"])
                )
                | Q(
                    # Existing availability starts within the new one's timeframe
                    Q(start_time__gte=data["start_time"])
                    & Q(start_time__lt=data["end_time"])
                )
                | Q(
                    # Existing availability ends within the new one's timeframe
                    Q(end_time__gt=data["start_time"])
                    & Q(end_time__lte=data["end_time"])
                )
            )
        )
        .exclude(is_temp=True)
        .exists()
    )

@role_required(allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value])
def remove_availability(request, id,action = None):
    qs = get_object_or_404(Avaliability, id=id)

    if action == 'del':
        avail_exists_in_booking = BookedMeeting.objects.filter(availability=qs).exists()
        if not avail_exists_in_booking:
            qs.delete()
            messages.success(request, "Availability successfully deleted.")
        else:
            messages.error(request,"Availability can not be removed as it was used in meeting bookings you can try disabling it, if already disabled.")
    else:
        qs.is_disabled = not qs.is_disabled
        qs.save()
        status = "enabled" if not qs.is_disabled else "disabled"
        messages.success(request, f"Availability successfully {status}.")
    
    return redirect("meeting_calendar:availability")

@role_required(allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value])
def book_a_meeting_v1(request, user_id):
    template_name = "book_a_meeting_v1.html"
    form = BookMeetingForm(request.POST or None)
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
       
        if form.is_valid():
            cleaned_data = form.cleaned_data
            booking_date = cleaned_data['booking_date']
            start_time = cleaned_data['start_time']
            end_time = cleaned_data['end_time']
            new_booking = BookedMeeting.objects.create(
                requester = request.user,
                requested = user,
                start_time = start_time,
                end_time = end_time,
                booking_date = booking_date
            )
            if new_booking:
                email_ = Email(
                    subject="Meeting request",
                    recipient_list=[new_booking.requested.email],
                    message=f"""
                    <p>New Meetings Details</p>
                    <p>Requester: {new_booking.requester.get_full_name().title()} </p>
                    <p>Date: {new_booking.booking_date} </p>
                    <p>Slot: {booking_date} from {start_time} to  {end_time} </p>
                
                    """,
                )            
                email_.send()
                messages.success(request, "Meeting request successfully sent")
        return redirect("accounts:public_profile", user.id)

    return render(request, template_name,{'form':form, 'obj':user})


@role_required(allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value])
def book_a_meeting(request, user_id):
    template_name = "book_a_meeting.html"
    user = get_object_or_404(User, id=user_id)
    has_availability = [av for av in user.user_availability.all() if not av.is_temp and not av.is_disabled]

    if request.method == "POST":
        day = request.POST.get("day")
        booking_date = request.POST.get("booking_date")
        availability = get_object_or_404(Avaliability, id=day)
        check_availability = check_meeting_exists(user, availability, booking_date)
        if check_availability:
            messages.error(
                request,
                f"The {availability.day.capitalize()} slot on {booking_date} from {availability.start_time.strftime('%H:%M')} to {availability.end_time.strftime('%H:%M')} is already booked.",
            )
            return redirect("meeting_calendar:book_a_meeting", user.id)
        new_booked_meeting = BookedMeeting.objects.create(
            requester=request.user,
            requested=user,
            booking_date=booking_date,
            availability=availability,
            notes=request.POST.get("notes"),
        )
        # base_url = request.build_absolute_uri('/')

        # link = f"{base_url}{new_booked_meeting.get_absolute_url()}"
        messages.success(request, "Meeting request successfully sent")
        email_ = Email(
            subject="Meeting request",
            recipient_list=[new_booked_meeting.requested.email],
            message=f"""
            <p>New Meetings Details</p>
            <p>Requester: {new_booked_meeting.requester.get_full_name().title()} </p>
            <p>Date: {new_booked_meeting.booking_date} </p>
            <p>Slot: {new_booked_meeting.availability.day}: {new_booked_meeting.availability.start_time} {new_booked_meeting.availability.end_time} </p>
        
            """,
        )
        print("sending email .......")
        print(email_)
        email_.send()
        return redirect("accounts:public_profile", user.id)
    return render(
        request,
        template_name,
        {
            "obj": user,
            "min_date": date.today().strftime("%Y-%m-%d"),
            "has_availability" :has_availability
        },
    )

def check_meeting_exists(requested_user, availability, booking_date):
    return BookedMeeting.objects.filter(
        Q(requested=requested_user)
        & Q(availability=availability)
        & Q(booking_date=booking_date)
        & Q(accepted=True)
    ).exists()

def get_availability(request, requested_user_id, booking_date):
    requested_user = get_object_or_404(User, id=requested_user_id)
    data = []
    for slot in requested_user.user_availability.all():
        if not check_meeting_exists(requested_user, slot, booking_date):
            data.append(
                {
                    "id": slot.id,
                    "day": slot.day,
                    "start_time": slot.start_time.strftime("%H:%M"),
                    "end_time": slot.end_time.strftime("%H:%M"),
                }
            )
    return JsonResponse(data, safe=False)

@role_required(allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value])
def meeting_detail(request, meeting_id):
    template_name = "meeting_detail.html"
    obj = get_object_or_404(BookedMeeting, id=meeting_id)
    is_checked_in, is_checked_out = check_status_func(request, obj)
    context = {
        "obj": obj,
        "current_date": date.today(),
        "is_checked_in": is_checked_in,
        "is_checked_out": is_checked_out,
    }
    return render(request, template_name, context)

def check_status_func(request, obj):
    check_status = MeetingCheckInAndOut.objects.filter(
        Q(booked_meeting=obj) & Q(user=request.user)
    )
    is_checked_in = check_status.filter(is_checked_in=True).exists()
    is_checked_out = check_status.filter(is_checked_out=True).exists()
    return is_checked_in, is_checked_out

@role_required(allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value])
def check_in_or_check_out(request, meeting_id, check_type):
    template_name = 'check_in_check_out.html'
    obj = get_object_or_404(BookedMeeting, id=meeting_id)

    if check_type not in ["check-in", "check-out"]:
        messages.error(request, "Invalid check type.")
        return redirect("meeting_calendar:meeting_detail", obj.id)

    is_checked_in, is_checked_out = check_status_func(request, obj)

    if check_type == "check-in":
        if is_checked_in:
            messages.error(request, "You have already checked in.")
        else:
            check_in_and_out_func(
                request, obj, is_checked_in_=True, is_checked_out_=False
            )
            messages.success(request, "Checked in successfully.")
    elif check_type == "check-out":
        if not is_checked_in:
            messages.error(request, "You need to check in first.")
        elif is_checked_out:
            messages.error(request, "You have already checked out.")
        else:
            check_in_and_out_func(
                request, obj, is_checked_in_=True, is_checked_out_=True
            )
            messages.success(request, "Checked out successfully.")

    return render(request, template_name)


def check_in_and_out_func(request, obj, is_checked_in_, is_checked_out_):
    MeetingCheckInAndOut.objects.create(
        booked_meeting=obj,
        user=request.user,
        is_checked_in=is_checked_in_,
        is_checked_out=is_checked_out_,
    )


@role_required(allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value])
def update_meeting_status(request, meeting_id, status_type):

    if status_type not in [
        MeetingStatusEnum.ACCEPTED.value,
        MeetingStatusEnum.REJECTED.value,
        MeetingStatusEnum.CANCELLED.value,
    ]:
        messages.error(request, "Invalid status type.")
        return redirect("meeting_calendar:meeting_detail", meeting_id)

    meeting = get_object_or_404(BookedMeeting, pk=meeting_id)


    if status_type == MeetingStatusEnum.CANCELLED.value:
        check_in_exists = MeetingCheckInAndOut.objects.filter(
            Q(booked_meeting=meeting)
            & (Q(user=meeting.requester) | Q(user=meeting.requested))
            & Q(is_checked_in=True)
        ).exists()
        if check_in_exists:
            messages.error(
                request,
                f"You can not cancel a checked in meeting by either requester or requested.",
            )
            return redirect('/')


    meeting.accepted = status_type == MeetingStatusEnum.ACCEPTED.value
    meeting.rejected = status_type == MeetingStatusEnum.REJECTED.value
    meeting.cancelled = status_type == MeetingStatusEnum.CANCELLED.value
    meeting.save()
    

    status_message_map = {
        MeetingStatusEnum.ACCEPTED.value: "accepted",
        MeetingStatusEnum.REJECTED.value: "rejected",
        MeetingStatusEnum.CANCELLED.value: "cancelled",
    }
    success_message = f"Meeting successfully {status_message_map[status_type]}."
    messages.success(request, success_message)
    if meeting.requested:
        email_ = Email(
            subject="Meeting Status",
            recipient_list=[meeting.requested.email, meeting.requester.email],
            message=f"""
            <p>Expected Meeting Attendees: {meeting.requested.get_full_name().title()} and {meeting.requester.get_full_name().title()}</p>
            <p>Meeting Status: {status_message_map[status_type]} </p>
            <p>Meeting Date: {meeting.booking_date} from : ({meeting.start_time} to {meeting.end_time})  </p>
            """,
        )
        email_.send()

    return redirect("/")


def extract_day_of_week(date_value):
    date_object = datetime.strptime(date_value, "%Y-%m-%d")
    day_number = date_object.weekday()
    weekdays = [
        DayEnum.MONDAY.value,
        DayEnum.TUESDAY.value,
        DayEnum.WEDNESDAY.value,
        DayEnum.THURSDAY.value,
        DayEnum.FRIDAY.value,
        DayEnum.SATURDAY.value,
        DayEnum.SUNDAY.value,
    ]
    return weekdays[day_number]


@role_required(allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value])
def create_a_quick_meeting(request):

    if request.method == "POST":
        form = QuickMeeting(request.POST or None)
        if form.is_valid():
            user_ = request.user
            date = request.POST.get("date")
            start_time=request.POST.get("start_time"),
            end_time=request.POST.get("end_time"),

            BookedMeeting.objects.create(
                requester=user_, start_time=start_time,end_time=end_time, booking_date=date
            )
            messages.success(request, "Meeting successfully broadcasted.")

    return redirect("/")

@role_required(allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value])
def availability_and_session_expectation(request):
    template_name = 'availability_and_session_expectation.html'
    user =  request.user
    obj = ''
    exists= SessionExpectationAndAvailabilityInfo.objects.filter(user = user).exists()
    if exists:
        obj = get_object_or_404(SessionExpectationAndAvailabilityInfo,user=user)
    else:
        obj = SessionExpectationAndAvailabilityInfo.objects.create(
            user=user,
            availability_and_session_expectation = "n/a"

        )

    form = SessionExpectationAndAvailabilityInfoForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()  
            messages.success(request,'Session expectations and availability successfully updated.')
            return redirect('accounts:profile')   
    return render(request, template_name,{'form':form,'obj':obj})

@role_required(allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value])
def accept_a_quick_meeting(request, id):
    meeting = get_object_or_404(BookedMeeting, id=id)
    user_ = request.user
    meeting.requested = user_
    meeting.accepted = True
    meeting.save()
    messages.success(
        request,
        f"You have successfully accepted a quick meeting from {meeting.requester.get_full_name()}",
    )
    email_ = Email(
        subject="Quick meeting acceptance",
        recipient_list=[meeting.requester.email],
        message=f"""
        <p>New Meetings Details</p>
        <p>Accepted by: {user_.get_full_name()} </p>
        <p>Date: {meeting.booking_date} </p>
        <p>Slot: {meeting.availability.day}: {meeting.availability.start_time} {meeting.availability.end_time} </p>
    
        """,
    )
    email_.send()
    return redirect("/")

def check_in_from_email(request, meeting_id):
    meeting = get_object_or_404(BookedMeeting, id = meeting_id)

    


