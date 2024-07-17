from datetime import date
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import (
  User,
  GeneralInfo,
  StudyBuddyAdditionalInfo
)
from meeting_calendar.models import (
    BookedMeeting
)


class ProfilePictureForm(forms.Form):
    profile_picture = forms.ImageField(
        help_text="Allowed JPG or PNG",
        widget= forms.FileInput(attrs={'accept': 'image/png, image/jpeg, image/jpg'}))

class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''

class LoginForm(forms.Form):
  username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
  password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control','id':'password-id'}))

  def clean(self):
    cleaned_data = super().clean()
    username = cleaned_data.get("username")
    password = cleaned_data.get("password")

    if not username or not password:
      raise forms.ValidationError("Please enter both username and password.")

    user = authenticate(username=username, password=password)
    if user and not user.is_active:
      raise forms.ValidationError("Your account is inactive. Please contact IMGSTUDYBUDDY.")

    return cleaned_data
  

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',]

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']

    def clean(self):    
        cleaned_data = super().clean()
        email = self.cleaned_data['email']
        print(f"email validation {email}")
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return cleaned_data

class GeneralInfoForm(forms.ModelForm):
    class Meta:
        model =  GeneralInfo
        fields = ['gender', 'time_zone', 'phone_number', 'profile_picture']

class StudyBuddyAdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = StudyBuddyAdditionalInfo
        widgets = {
            'exam_date': forms.widgets.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date', 'min':date.today()})
        }
        fields = ['exam_date']

class LoginInfoForm(forms.Form):
    email = forms.CharField(label="email", max_length=30, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control','id':'password-id'}))