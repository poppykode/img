from django.shortcuts import render
from . import forms

# Create your views here.
def success(request):
    template_name = 'success.html'
    return render(request, template_name)

def cancel(request):
    template_name = 'cancel.html'
    return render(request, template_name)

# check if already subscribed
# gray out subscription
# can upgrade subscription


