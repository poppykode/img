from django import forms
from django.contrib.auth import authenticate
from accounts.models import (
  User,
 StudyBuddyGeneralInfo,
  StudyBuddyAdditionalInfo

)

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

class StudyBuddyGeneralInfoForm(forms.ModelForm):
    class Meta:
        model =  StudyBuddyGeneralInfo
        fields = ['gender', 'time_zone', 'phone_number', 'profile_picture']

class StudyBuddyAdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = StudyBuddyAdditionalInfo
        widgets = {
            "exam_date": forms.DateInput(attrs={"class": "datepicker", "type": "date"})
        }
        fields = ['exam_date']

class LoginInfoForm(forms.Form):
    email = forms.CharField(label="email", max_length=30, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control','id':'password-id'}))
