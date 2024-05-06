from django.contrib.auth import authenticate, login as login_, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.decorators import is_authenticated
from core.enums import RoleEnum
from accounts.forms import LoginForm


@is_authenticated
def login(request):
    template_name = 'registration/login.html'
    form =  LoginForm(request.POST or None)
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
    return render(request,template_name)


@login_required
def redirect_logged(request):
    user = request.user.role
    if user == RoleEnum.ADMIN.value:
        return redirect('accounts:admin_dashboard')
    elif user == RoleEnum.CANDIDATE.value:
        return redirect('accounts:candidate_dashboard')
    elif user == RoleEnum.COACH.value:
        return redirect('accounts:coach_dashboard')
    else:
        messages.error(request,'You do not have a role assigned.')
        return redirect('accounts:not_authorized')
    
@login_required
def my_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('/')

