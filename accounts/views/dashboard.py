
import os
from django.db.models import Q
from datetime import datetime, date
from accounts.models import User
from core.email import Email
from core.enums import RoleEnum
from core.utils import generate_password, paginator
from meeting_calendar.forms import QuickMeeting
from offers.models import Offer
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
# import plotly.express as px
# import pandas as pd
# from plotly.offline import plot

from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.forms import AdminUserForm, ProfilePictureForm, PasswordChangeForm, MyPasswordChangeForm, StudyBuddyAdditionalInfoForm, UserForm, GeneralInfoForm
from accounts.models import GeneralInfo, StudyBuddyAdditionalInfo
from meeting_calendar.models import BookedMeeting, MeetingCheckInAndOut



@login_required  
def candidate_dashboard(request):
    template_name = 'dashboards/candidate_dashboard.html'
    user = request.user
    meetings = BookedMeeting.objects.for_user(user)
    quick_meetings = BookedMeeting.objects.quick_meetings(user)
    rejected_count = meetings.filter(rejected = True).count()
    accepted_count = meetings.filter(accepted = True).count()
    cancelled_count = meetings.filter(cancelled = True).count()
    check_in_and_out_count = MeetingCheckInAndOut.objects.filter(
        Q(user=request.user) 
        & Q(is_checked_in=True) 
        & Q(is_checked_out=True)
    ).count()
    context = {
        'items': paginator(request,meetings,25) ,
        'user':user,
        'current_date': date.today(),
        'rejected_count':rejected_count,
        'accepted_count':accepted_count,
        'cancelled_count':cancelled_count,
        'check_in_and_out_count':check_in_and_out_count,
        'total_meetimgs':meetings.count(),
        'form':QuickMeeting(),
        'quick_meetings': quick_meetings

    }
    return render(request, template_name,context)

@login_required  
def coach_dashboard(request):
    template_name = 'dashboards/coach_dashboard.html'
    date_today = date.today()
    user = request.user
    # user_ = get_object_or_404(models.User,id=user.id)
    # was_attended_no_res = models.Meeting.objects.filter(requested = user).filter(was_meeting_accepted=True).filter(was_meeting_attended = None).filter(date__lt = date_today)
    return render(request, template_name)

@login_required  
def admin_dashboard(request):
    template_name = 'dashboards/admin_dashboard.html'
    # meetings = Meeting.objects.all()
    # qs = models.User.objects.all()
    # accepted = len(qs.filter(is_coach=True).filter(account_status = 'accepted'))
    # pending = len(qs.filter(is_coach=True).filter(account_status = 'pending'))
    # rejected = len(qs.filter(is_coach=True).filter(account_status = 'rejected'))
    # values = [accepted, pending,rejected]
    names =  ["Accepted","Pending","Rejected"]
    # df = px.data.iris()
    # fig = px.pie(df,values=values, names=names)
    # pie_chart = plot(fig, output_type="div")
    # offers = Offer.objects.filter(status='pending')
    context ={
        # 'users':qs,
        # "pie_chart":pie_chart,
        # 'meetings':meetings,
        # 'offers':offers,
        # 'number_of_offers':len(offers)
    }
    return render(request, template_name,context)


@login_required
def profile(request):
    template_name =  'registration/profile.html'
    user_qs = get_object_or_404(User, pk=request.user.pk)
    return render(request,template_name, {'obj':user_qs})

@login_required
def public_profile(request,user_id):
    template_name =  'registration/public_profile.html'
    user_qs = get_object_or_404(User, id=user_id)
    offers = Offer.objects.filter(user=user_qs).filter(status ='accepted')
    form = ''
    return render(request,template_name, {'obj':user_qs,'form':form,'offers':offers})

@login_required
def users(request):
    template_name =  'registration/users.html'

    user_qs = User.objects.exclude(id=request.user.id)
    return render(request,template_name, {'users':paginator(request,user_qs,25)})

@login_required
def admin_profile(request,coach_id):
    template_name =  'registration/admin_profile.html'
    coach_qs = get_object_or_404(User,id=coach_id)
    return render(request,template_name, {'obj':coach_qs})

@login_required
def activate_or_deactivate_account(request,user_id):
    url = request.META.get('HTTP_REFERER')
    user = get_object_or_404(User,id=user_id)
    is_active =''
    msg = ''

    if user.is_active:
        is_active = False
        msg='deactivated'
    else:
        is_active=True
        msg='activated'
    user.is_active = is_active
    user.save()
    if request.user.id == user_id:
        auth.logout(request)
    messages.success(request,'Account has been successfully '+ msg)
    return redirect(url)

@login_required
def add_admin(request):
    template_name = 'registration/add_admin.html'
    form = AdminUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
            email = cleaned_data['email']
            generated_password = generate_password()
            user = User.objects.create_user(username=email, email=email, password=generated_password)
            user.first_name = cleaned_data['first_name']
            user.last_name = cleaned_data['last_name']
            user.role = RoleEnum.ADMIN.value
            user.is_active = True
            user.save()
            email_ = Email(
                subject="New account creation",
                recipient_list=[email],
                message=f"""
                <p>Account Details</p>
                <p>Username: {email} </p>
                <p>Password: {generated_password} </p>
                """

            )
            email_.send()
            messages.success(request,'User successfully added.')
            return redirect('accounts:users')

    return render(request,template_name, {"form":form})


@login_required
def update_general_additional_info(request):
    template_name = 'registration/update_general_additional_info.html'
    obj = get_object_or_404(GeneralInfo, user = request.user)
    if request.method == 'POST':
        form = GeneralInfoForm(request.POST, instance=obj)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            obj.gender = cleaned_data['gender']
            obj.time_zone = cleaned_data['time_zone']
            obj.phone_number = cleaned_data['phone_number']
            obj.save()
            messages.success(request,'Info successfully updated.')
            return redirect('accounts:profile')
    form = GeneralInfoForm(instance=obj)
    return render(request,template_name,{'obj':obj,'form':form})


@login_required
def update_personal_details(request):
    template_name = 'registration/update_personal_details.html'
    obj = get_object_or_404(User, id = request.user.id)
    if request.method == 'POST':
        form = AdminUserForm(request.POST, instance=obj)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            obj.username = cleaned_data['email']
            obj.email= cleaned_data['email']
            obj.first_name = cleaned_data['first_name']
            obj.last_name = cleaned_data['last_name']
            obj.save()
            messages.success(request,'Info successfully updated.')
            return redirect('accounts:profile')
    form = AdminUserForm(instance=obj)
    return render(request,template_name,{'obj':obj,'form':form})

@login_required
def upload_profile_picture(request):
    template_name = 'registration/upload_profile_picture.html'
    user_qs = get_object_or_404(GeneralInfo, user=request.user.id)
    form = ProfilePictureForm()
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST,request.FILES)
        if form.is_valid():
            user_qs.profile_picture = form.cleaned_data["profile_picture"]
            user_qs.save()
            messages.success(request, 'Profile picture successfully uploaded.')
            return redirect('accounts:profile')
        else:
            messages.error(request,f"Something went wrong with {form.errors}")
            args = {'form': form, 'obj': user_qs}
            return render(request, template_name, args)
    else:
        args = {'form': form, 'obj': user_qs}
        return render(request, template_name, args)


@login_required
def update_exam_date(request):
    template_name = 'registration/update_exam_date.html'
    obj = get_object_or_404(StudyBuddyAdditionalInfo, user = request.user)
    if request.method == 'POST':
        form = StudyBuddyAdditionalInfoForm(request.POST, instance=obj)
        if form.is_valid():         
            obj.exam_date = form.cleaned_data['exam_date']
            obj.save()
            messages.success(request,'Info successfully updated.')
            return redirect('accounts:profile')
    form = StudyBuddyAdditionalInfoForm(instance=obj)
    return render(request,template_name,{'obj':obj,'form':form})


@login_required
def change_password(request):
    user_qs = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = MyPasswordChangeForm(data=request.POST, user=user_qs)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password successfully changed.')
            return redirect('accounts:profile')
        else:
            messages.error(request,f"Something went wrong with {form.errors}")
            return redirect('accounts:profile')
    else:
        form = MyPasswordChangeForm(user=user_qs)
        args = {'form': form, 'obj': user_qs}
        return render(request, 'registration/change_password.html', args)