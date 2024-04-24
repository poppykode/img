from django import forms
from . import models

form_control = {'class': 'form-control'}

class StationForm(forms.ModelForm):
  class Meta:
    model = models.Station
    widgets = {
      'title': forms.widgets.TextInput(attrs=form_control)
    }
    labels = {
        'title':'Station Name'
    }
    fields = ['title',]

class StationCategoryForm(forms.ModelForm):
  class Meta:
    model = models.StationCategory
    widgets = {
      'title': forms.widgets.TextInput(attrs=form_control)
    }
    labels = {
        'title':'Station Category Name'
    }

    fields = ['station','title',]

class StationSubCategoryForm(forms.ModelForm):
  class Meta:
    model = models.StationSubCategory
    widgets = {
      'title': forms.widgets.TextInput(attrs=form_control)
    }
    labels = {
        'title':'Station Sub Category Name'
    }
    fields = ['station_category','title',]

