from django import forms
from . import models

class AvaliabilityForm(forms.ModelForm):
    class Meta:
        model = models.Avaliability
        fields = (
            'day',
            'start_time',
            'end_time'
        )