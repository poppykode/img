from django import forms
from . import models

form_control = {'class': 'form-control'}

def get_all_stations():
    stations = models.ThirdLevelStation.objects.all()
    choices = [(station.id, station.title) for station in stations]
    return choices

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

class StationForm(forms.Form):
  station = forms.ChoiceField(label="Station", choices=get_all_stations())


class CandidateInstructionForm(forms.ModelForm):
  class Meta:
    model = models.CandidateInstruction
    widgets = {
      'heading': forms.widgets.Select(attrs={'class':'form-select form-control'}),
      'text': forms.widgets.Textarea(attrs={'class':'form-control','rows':1})
    }
    fields = ['heading','text',]

class PatientDisclosureForm(forms.ModelForm):
  class Meta:
    model = models.PatientInstruction
    widgets = {
      'heading': forms.widgets.Select(attrs={'class':'form-select form-control'}),
      'text': forms.widgets.Textarea(attrs={'class':'form-control','rows':1})
    }
    fields = ['heading','text',]

class ExaminerMarkSheetForm(forms.ModelForm):
  class Meta:
    model = models.ExaminerMarkSheet
    widgets = {
      'heading': forms.widgets.Select(attrs={'class':'form-select form-control'})
    }
    fields = ['heading']



