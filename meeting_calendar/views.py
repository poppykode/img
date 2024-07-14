import calendar
from django.db.models import Q
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from core.decorators import role_required
from core.enums import RoleEnum, MeetingStatusEnum
from meeting_calendar.forms import AvaliabilityForm
from .utils import Calendar
from .models import BookedMeeting, Avaliability, MeetingCheckInAndOut
from datetime import datetime, timedelta, date
from accounts.models import User


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
    allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value, RoleEnum.COACH.value]
)
def availability(request, user_id=None):
    template_name = "availability.html"
    if not user_id:
        if request.user:
            is_avaliability = Avaliability.objects.filter(user=request.user).exists()
            request.session["has_availabilty"] = is_avaliability
    user = request.user
    qs = Avaliability.objects.filter(user=user)
    if user_id:
        user_ = get_object_or_404(User, id=user_id)
        user = user_
        qs = Avaliability.objects.filter(user=user_)
    return render(request, template_name, {"avail": qs, "user": user})


@role_required(
    allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value]
)
def create_availability(request):
    template_name = "create_availability.html"
    form = AvaliabilityForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            if is_overlapping_availabilities_func(request,form.cleaned_data):
                messages.error(request, "This availability overlaps with an existing one. Please choose a different time slot.")
                return redirect("meeting_calendar:create_availability")
            
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Availability successfully added.")
            return redirect("meeting_calendar:availability")

    return render(request, template_name, {"form": form, "type": "create"})

def is_overlapping_availabilities_func(request, data):
    return Avaliability.objects.filter(
        Q(user=request.user) 
        & Q(day=data['day'])
        & (
            Q(  # Overlap scenarios:
                # Existing availability starts before and ends after the new one
                Q(start_time__lt= data['start_time']) & Q(end_time__gt= data['end_time'])
            ) | Q(
                # Existing availability starts within the new one's timeframe
                Q(start_time__gte=data['start_time']) & Q(start_time__lt=data['end_time'])
            ) | Q(
                # Existing availability ends within the new one's timeframe
                Q(end_time__gt=data['start_time']) & Q(end_time__lte=data['end_time'])
            )
        )
    ).exists()


@role_required(
    allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value]
)
def remove_availability(request, id):
    qs = get_object_or_404(Avaliability, id=id)
    qs.delete()
    messages.success(request, "Availability successfully deleted.")
    return redirect("meeting_calendar:availability")


@role_required(
    allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value]
)
def book_a_meeting(request, user_id):
    template_name = "book_a_meeting.html"
    user = get_object_or_404(User, id=user_id)
    # check if slot is booked
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
        BookedMeeting.objects.create(
            requester=request.user,
            requested=user,
            booking_date=booking_date,
            availability=availability,
            notes = request.POST.get("notes")
        )
        messages.success(request, "Meeting request successfully sent")
        # send email
        return redirect("accounts:public_profile", user.id)
    return render(request, template_name, {"obj": user, 'min_date': date.today().strftime('%Y-%m-%d'),})


def check_meeting_exists(requested_user, availability, booking_date):
    return BookedMeeting.objects.filter(
        Q(requested=requested_user)
        & Q(availability=availability)
        & Q(booking_date=booking_date)
        & Q(accepted = True)       
    ).exists()


def get_availability(request, requested_user_id, booking_date):
    requested_user = get_object_or_404(User, id=requested_user_id)
    data = []
    for slot in requested_user.user_availability.all():
        print(f"slot {slot}")
        print(check_meeting_exists(requested_user, slot, booking_date))
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

@role_required(
    allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value]
)
def meeting_detail(request, meeting_id):
    template_name = 'meeting_detail.html'
    obj = get_object_or_404(BookedMeeting, id = meeting_id)
    is_checked_in, is_checked_out = check_status_func(request, obj)
    context = {
        'obj':obj,
        'current_date':date.today(),
        'is_checked_in':is_checked_in,
        'is_checked_out':is_checked_out
    }
    return render(request, template_name,context)

def check_status_func(request, obj):
    check_status = MeetingCheckInAndOut.objects.filter(
        Q(booked_meeting = obj)
        & Q(user = request.user)
    )
    is_checked_in = check_status.filter(is_checked_in = True).exists()
    is_checked_out = check_status.filter(is_checked_out = True).exists()
    return is_checked_in,is_checked_out

@role_required(
    allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value]
)
def check_in_or_check_out(request, meeting_id, check_type):
    obj = get_object_or_404(BookedMeeting, id=meeting_id)
    
    if check_type not in ['check-in', 'check-out']:
        messages.error(request, "Invalid check type.")
        return redirect('meeting_calendar:meeting_detail', obj.id)

    is_checked_in, is_checked_out = check_status_func(request, obj)
    
    if check_type == 'check-in':
        if is_checked_in:
            messages.error(request, "You have already checked in.")
        else:
            check_in_and_out_func(request, obj, is_checked_in_=True, is_checked_out_=False)
            messages.success(request, "Checked in successfully.")
    elif check_type == 'check-out':
        if not is_checked_in:
            messages.error(request, "You need to check in first.")
        elif is_checked_out:
            messages.error(request, "You have already checked out.")
        else:
            check_in_and_out_func(request, obj, is_checked_in_=True, is_checked_out_=True)
            messages.success(request, "Checked out successfully.")
    
    return redirect('meeting_calendar:meeting_detail', obj.id)

def check_in_and_out_func(request, obj, is_checked_in_, is_checked_out_):
    MeetingCheckInAndOut.objects.create(
        booked_meeting = obj,
        user = request.user,
        is_checked_in = is_checked_in_,
        is_checked_out = is_checked_out_
    )

@role_required(
    allowed_roles=[RoleEnum.CANDIDATE.value, RoleEnum.COACH.value]
)
def update_meeting_status(request, meeting_id, status_type):

    if status_type not in  [MeetingStatusEnum.ACCEPTED.value, MeetingStatusEnum.REJECTED.value, MeetingStatusEnum.CANCELLED.value]:
        messages.error(request, "Invalid status type.")
        return redirect('meeting_calendar:meeting_detail', meeting_id)

    meeting = get_object_or_404(BookedMeeting, pk=meeting_id)

    if status_type == MeetingStatusEnum.CANCELLED.value:
        check_in_exists = MeetingCheckInAndOut.objects.filter(
            Q(booked_meeting=meeting)
            & (Q(user=meeting.requester) | Q(user=meeting.requested))
            & Q(is_checked_in=True)
        ).exists()
        if check_in_exists:
            messages.error(request, f"You can not cancel a checked in meeting by either requester or requested.")
            return redirect('meeting_calendar:meeting_detail', meeting_id)

    meeting.accepted = (status_type == MeetingStatusEnum.ACCEPTED.value)
    meeting.rejected = (status_type == MeetingStatusEnum.REJECTED.value)
    meeting.cancelled = (status_type == MeetingStatusEnum.CANCELLED.value)
    meeting.save()

    status_message_map = {
        MeetingStatusEnum.ACCEPTED.value: "accepted",
        MeetingStatusEnum.REJECTED.value: "rejected",
        MeetingStatusEnum.CANCELLED.value: "cancelled",
    }
    success_message = f"Meeting successfully {status_message_map[status_type]}."
    messages.success(request, success_message)

    # Send email

    return redirect('meeting_calendar:meeting_detail', meeting.id)
