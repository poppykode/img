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
    fields = ['title','interval','is_active','duration_period','price',]


class SubscriptionForm(forms.Form):
  date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))
  date_to = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control','type':'date'}))


