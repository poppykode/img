from django import forms
from . import models

form_control = {'class': 'form-control'}

class FirstLevelStationForm(forms.ModelForm):
  class Meta:
    model = models.FirstLevelStation
    widgets = {
      'title': forms.widgets.TextInput(attrs=form_control)
    }
    labels = {
        'title':'First Level Station Name'
    }
    fields = ['title',]

class SecondLevelStationForm(forms.ModelForm):
  class Meta:
    model = models.SecondLevelStation
    widgets = {
      'title': forms.widgets.TextInput(attrs=form_control)
    }
    labels = {
        'title':'Second Level Station Name'
    }

    fields = ['first_level_station','title',]

class ThirdLevelStationForm(forms.ModelForm):
  class Meta:
    model = models.ThirdLevelStation
    widgets = {
      'title': forms.widgets.TextInput(attrs=form_control)
    }
    labels = {
        'title':'Third Level Station Name'
    }
    fields = ['second_level_station','title',]

