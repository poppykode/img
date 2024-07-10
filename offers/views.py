import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from .forms import OfferForm
# Create your views here.

@login_required
def offer_details(request,offer_id):
    template_name = 'offer_details.html'
    obj = get_object_or_404(models.Offer,id=offer_id)
    context ={'obj':obj}
    return render(request,template_name,context)

@login_required
def offers(request):
    template_name = 'offers.html'
    offers_qs = models.Offer.objects.filter(user = request.user)
    context = {
        "offers":offers_qs
    }
    return render(request,template_name,context)

@login_required
def create_offer(request):
    template_name = 'create_offer.html'
    form = OfferForm(request.POST or None,request.FILES or None)
    print(form.errors.as_data())
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request,"offer successfully added.")
            return redirect("offers:offers")
    return render(request,template_name, {'form':form})

@login_required
def create_offer_json(request):
    if request.method == 'POST':
        user=request.user
        title=request.POST.get('title')
        image=request.FILES.get('image')
        summary =request.POST.get('summary')
        description =request.POST.get('description')
        price = request.POST.get('price')
        print("title >>>" + title)
        print("description >>>" + description)
        new_offer = models.Offer(user=user,title=title,image=image,description=description,summary=summary,price=price)
        new_offer.save()
        data = {'title':new_offer.title,'summary':new_offer.summary,'description':new_offer.description,'price':new_offer.price,'image':new_offer.image.url }
        return JsonResponse(data)
    return JsonResponse({"error":"something went wrong"})

@login_required
def accept_or_reject_offer(request,offer_id,status):
    obj = get_object_or_404(models.Offer,id=offer_id)
    subject = 'Offer content was not approved.'
    message = f'Hi, {obj.user.get_full_name()}, your content offer was not approved.'
    obj.status = status
    obj.save()
    if status == 'accepted':
        subject ='Offer content was approved'
        message = f'Hi, {obj.user.get_full_name()}, congradulations, your content offer titled "{obj.title}" was approved.'
    messages.success(request,"Offer was successfully {}".format(status))
    # Send email for decline or approval
    return redirect('/')