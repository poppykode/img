import calendar
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, get_object_or_404,redirect

from core.decorators import role_required
from core.enums import RoleEnum
from meeting_calendar.forms import AvaliabilityForm
from .utils import Calendar
from .models import BookedMeeting, Avaliability, MeetingCheckInAndOut
from datetime import datetime,timedelta, date 



class CalendarView(generic.ListView):
    model = BookedMeeting
    template_name = 'calendar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        qs = None

        user = self.request.user
        qs = BookedMeeting.objects.filter(start_date__year=d.year, start_date__month=d.month,requested = user)  
        cal = Calendar()
        html_cal = cal.formatmonth(withyear=True, qs=qs,y=d.year,m=d.month)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def availability(request):
    template_name = 'availability.html'
    qs = Avaliability.objects.all()
    return render(request,template_name,{'avail':qs})
    

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_availability(request):
    template_name = 'create_availability.html'
    form  = AvaliabilityForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request,'Availability successfully added.')
            return redirect('meeting_calendar:availability')
    return render(request, template_name,{'form':form,'type':'create'})

@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def remove_availability(request, id):
    qs = get_object_or_404(Avaliability, id = id)
    qs.delete()
    messages.success(request, "Availability successfully deleted.")
    return redirect("meeting_calendar:availability")

@role_required(allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value])
def check_in_or_check_out(request, meeting_id, check_type):
    booked_meeting = get_object_or_404(BookedMeeting, id = meeting_id)
    if check_type == 'check_in':   
        MeetingCheckInAndOut.objects.create(
            booked_meeting = booked_meeting,
            is_checked_in = True
        )
        messages.success(request,'You have successfully checked in.')
    else:
        MeetingCheckInAndOut.objects.create(
        booked_meeting = booked_meeting,
        is_checked_out = True
        )
        messages.success(request,'You have successfully checked out.')
    return redirect("/")




    
    qs = get_object_or_404(Avaliability, id = id)
    qs.delete()
    messages.success(request, "Availability successfully deleted.")
    return redirect("meeting_calendar:availability")
    
    


