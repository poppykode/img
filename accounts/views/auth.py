from django.contrib.auth import authenticate, login as login_, logout
from django.core.files.storage import DefaultStorage
from formtools.wizard.views import SessionWizardView
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import is_authenticated
from core.enums import RoleEnum
from accounts import forms
from meeting_calendar.forms import AvaliabilityForm
from accounts.models import (
    User,
    GeneralInfo,
    StudyBuddyAdditionalInfo
)
from meeting_calendar.models import Avaliability


@is_authenticated
def login(request):
    template_name = 'registration/login.html'
    form =  forms.LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login_(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('accounts:redirect_logged')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        messages.error(request, form.errors) 
    return render(request, template_name,{'form':form})


def not_authorized(request):
    template_name = 'registration/not_authorized.html'
    return render(request,template_name,{'msg':request.user.role})


@login_required
def redirect_logged(request):
    user_role = request.user.role
    request.session['has_availabilty'] = Avaliability.objects.filter(user = request.user).exists()
    if user_role == RoleEnum.ADMIN.value:
        return redirect('subscriptions:subscriptions')
    elif user_role == RoleEnum.CANDIDATE.value:
        return redirect('meeting_calendar:meetings')
    elif user_role == RoleEnum.COACH.value:
        return redirect('accounts:coach_dashboard')
    else:
        messages.error(request,'You do not have a role assigned.')
        return redirect('accounts:not_authorized')
    
@login_required
def my_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('/')


class StudyBuddyDataWizard(SessionWizardView):
    form_list = [
        forms.UserForm,
        forms.GeneralInfoForm,
        forms.StudyBuddyAdditionalInfoForm,
        AvaliabilityForm,
        forms.LoginInfoForm
    ]
    file_storage = DefaultStorage()
    template_name = "registration/study_buddy_registration.html"

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        user_form = form_data[0]
        study_buddy_gen_info_form = form_data[1]
        study_buddy_add_info_form = form_data[2]
        study_buddy_add_availability = form_data[3]
        login_info_form = form_data[4]

        user = User.objects.create_user(username=login_info_form['email'], email=login_info_form['email'], password=login_info_form['password'])
        user.first_name = user_form['first_name']
        user.last_name = user_form['last_name']
        user.role = RoleEnum.CANDIDATE.value
        user.is_active = True
        user.save()

        GeneralInfo.objects.create(
            user = user,
            gender = study_buddy_gen_info_form['gender'],
            time_zone = study_buddy_gen_info_form['time_zone'],
            phone_number = study_buddy_gen_info_form['phone_number'],
            profile_picture = study_buddy_gen_info_form['profile_picture'],

        )
        Avaliability.objects.create(
            user=user,
            day = study_buddy_add_availability['day'],
            start_time =  study_buddy_add_availability['start_time'],
            end_time =  study_buddy_add_availability['end_time']
        )
    

        StudyBuddyAdditionalInfo.objects.create(
            user = user,
            exam_date = study_buddy_add_info_form['exam_date']
        )

        return redirect("/")


@login_required
def update_study_buddy_additional_info(request, id):
    obj = get_object_or_404(StudyBuddyAdditionalInfo, id=id)
    form = forms.StudyBuddyAdditionalInfoForm(request.POST or None, instance=obj)
    template_name = "update_study_buddy_additional_info.html"
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated.")
            return redirect("/")
    return render(
        request, template_name, {"form": form, "obj": obj}
    )
  
