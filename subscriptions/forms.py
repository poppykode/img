from django import forms
from . import models

form_control = {'class': 'form-control'}


class SubscriptionProductForm(forms.ModelForm):
  class Meta:
    model = models.SubscriptionProduct
    widgets = {
      'title': forms.widgets.TextInput(attrs=form_control),
      'is_active': forms.widgets.CheckboxInput()
    }
    labels = {
        'duration_period':'Duration of Subscription'
    }
    fields = ['title','interval','currency','is_active','duration_period','price',]
