from django import forms
from . import models
from tinymce.widgets import TinyMCE

class OfferForm(forms.ModelForm):
    class Meta:
        model = models.Offer
        widgets = {
          'summary': TinyMCE(attrs={'rows':4}),
          'description': TinyMCE(attrs={'rows':4}),
          'file': forms.FileInput(attrs={'accept': 'application/pdf'}),
          'image': forms.FileInput(attrs={'accept': 'image/png, image/jpeg, image/jpg'})
        }
        fields = ('title','image','file','summary','description','price')


