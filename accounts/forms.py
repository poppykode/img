from django import forms
from django.contrib.auth import authenticate

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
