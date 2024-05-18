import stripe
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from core.enums import RoleEnum
from core.decorators import role_required
from . import forms
from . import models


SECRET_KEY = settings.STRIPE_SECRET_KEY
BASE_URL = settings.BASE_URL

stripe.api_key = SECRET_KEY

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
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_subscription_product(request):
    template_name = 'subscription_products/create_subscription_product.html'
    form = forms.SubscriptionProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Subcription successfully created.')
        return redirect('subscriptions:subscription_products')
    return render(request, template_name,{'form':form})

@role_required(allowed_roles=[RoleEnum.ADMIN.value,RoleEnum.CANDIDATE.value])
def subscription_products(request):
    template_name = 'subscription_products/subscription_products.html'
    subscription_products = models.SubscriptionProduct.objects.filter(is_active = True)
    return render(request,template_name,{'items':subscription_products})


@role_required(allowed_roles=[RoleEnum.ADMIN.value,RoleEnum.CANDIDATE.value])
def subscribe(request, product_id):
    obj = get_object_or_404(models.SubscriptionProduct, id=product_id)
    success_path = reverse('subscriptions:success')
    cancel_path = reverse('subscriptions:cancel')
    success_url = f'{BASE_URL}{success_path}'
    cancel_url = f'{BASE_URL}{cancel_path}'
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price": obj.stripe_price_id,
                "quantity": 1
            }
        ],
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url
    )

    return HttpResponseRedirect(checkout_session.url)








