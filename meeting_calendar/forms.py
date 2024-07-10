from django.db.models import Q
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
            
            raise forms.ValidationError("End time must be after start time.")

        conflicting_availability = models.Avaliability.objects.filter(
            Q(day=day),
            Q(
                Q(start_time__lte=end_time) & Q(end_time__gte=start_time)  # Overlapping availability
                | Q(start_time__gte=start_time) & Q(end_time__lte=end_time)  # Availability entirely within selected times
                | Q(start_time__lt=start_time) & Q(end_time__gt=end_time)  # Availability surrounds selected times
            ),
        )

        if conflicting_availability.exists():
            raise forms.ValidationError("This availability overlaps with an existing availability.")

        return cleaned_data
