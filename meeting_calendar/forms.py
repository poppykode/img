from django.db.models import Q
from datetime import date
from django import forms
from . import models

        
class AvaliabilityForm(forms.ModelForm):
    class Meta:
        model = models.Avaliability
        widgets = {
            "start_time": forms.TimeInput(attrs={"class": "datepicker", "type": "time"}),
            "end_time": forms.TimeInput(attrs={"class": "datepicker", "type": "time"}),
        }
        fields = ("day", "start_time", "end_time")

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        day = cleaned_data.get("day")

        if start_time >= end_time:
            
            raise forms.ValidationError("Start time cannot be after end time.")

    
        return cleaned_data
    
class BookMeetingForm(forms.Form):
    day = forms.ModelChoiceField(queryset=None, empty_label=None) 

    def __init__(self, *args, user_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user_id:
            self.fields['day'].queryset = models.Avaliability.objects.filter(user=user_id)


class QuickMeeting(forms.Form):
    date =  forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker', 'data-date-format': 'YYYY-MM-DD', 'type': 'date','min':date.today()}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={"class": "datepicker", "type": "time"}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={"class": "datepicker", "type": "time"}))

    def clean(self):
        cleaned_data = super().clean()  

        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time and start_time > end_time:
            raise forms.ValidationError('Start time cannot be after end time.')

        return cleaned_data
