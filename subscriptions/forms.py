from django import forms
from . import models

form_control = {'class': 'form-control'}


class SubscriptionProductForm(forms.ModelForm):
  class Meta:
    model = models.SubscriptionProduct
    widgets = {
      'title': forms.widgets.TextInput(attrs=form_control)
    }
    labels = {
        'duration_period':'Duration of Subscription'
    }
    fields = ['title','interval','currency','duration_period','price','description',]
