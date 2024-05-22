import stripe
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from core.enums import RoleEnum
from core.decorators import role_required
from . import forms
from . import models
from . import utils


SECRET_KEY = settings.STRIPE_SECRET_KEY
BASE_URL = settings.BASE_URL

stripe.api_key = SECRET_KEY


# Create your views here.
@role_required(allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value])
def success(request):
    messages.success(request, "Subscription was successfull")
    return redirect("subscriptions:subscription_products")


@role_required(allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value])
def cancel(request):
    messages.error(request, "Subscription was cancelled.")
    return redirect("subscriptions:subscription_products")


# check if already subscribed
# gray out subscription
# can upgrade subscription
@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def create_subscription_product(request):
    template_name = "subscription_products/create_subscription_product.html"
    form = forms.SubscriptionProductForm(request.POST or None)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        stripe_product_id, stripe_price_id, stripe_price_in_cents = utils.create_stripe(
            cleaned_data["title"],
            cleaned_data["currency"],
            float(cleaned_data["price"])
        )
        new_sub_form = form.save(commit=False)
        new_sub_form.stripe_price = stripe_price_in_cents
        new_sub_form.stripe_product_id = stripe_product_id
        new_sub_form.stripe_price_id = stripe_price_id
        new_sub_form.save()
        messages.success(request, "Subcription successfully created.")
        return redirect("subscriptions:subscription_products")
    return render(request, template_name, {"form": form, "type": "create"})


@role_required(allowed_roles=[RoleEnum.ADMIN.value])
def edit_subscription_product(request, product_id):
    template_name = "subscription_products/create_subscription_product.html"
    obj = get_object_or_404(models.SubscriptionProduct, id=product_id)
    form = forms.SubscriptionProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        print(type(cleaned_data["price"]))
        try:
            utils.edit_stripe(obj, cleaned_data["title"],cleaned_data["currency"],cleaned_data["price"])
            form.save()
            messages.success(request, "Subscription successfully updated.")
        except Exception as e:
            messages.error(request, f"Error updating subscription: {e}")
        return redirect("subscriptions:subscription_products")

    return render(request, template_name, {"form": form, "type": "edit", "obj": obj})


@role_required(allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value])
def subscription_products(request):
    template_name = "subscription_products/subscription_products.html"
    subscription_products = models.SubscriptionProduct.objects.filter(is_active=True)
    return render(request, template_name, {"items": subscription_products})


@role_required(allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value])
def subscribe(request, product_id):
    obj = get_object_or_404(models.SubscriptionProduct, id=product_id)
    success_path = reverse("subscriptions:success")
    cancel_path = reverse("subscriptions:cancel")
    success_url = f"{BASE_URL}{success_path}"
    cancel_url = f"{BASE_URL}{cancel_path}"
    checkout_session = stripe.checkout.Session.create(
        line_items=[{"price": obj.stripe_price_id, "quantity": 1}],
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url,
    )

    return HttpResponseRedirect(checkout_session.url)
