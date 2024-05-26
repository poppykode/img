import stripe, logging
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
def success(request,sub_id):
    checkout_session_id = request.session.get('checkout_session_id')
    if checkout_session_id:
        obj = utils.successful_subscription(checkout_session_id,sub_id)
        logging.info(obj.id)
        del request.session['checkout_session_id']  
    else:
        logging.error(f"Check session id does not exist.")
    messages.success(request, "Subscription was successfull")
    return redirect("subscriptions:subscription_products")


@role_required(allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value])
def cancel(request):
    checkout_session_id = request.session.get('checkout_session_id')
    if checkout_session_id:
        obj = utils.unsuccessful_subscription(checkout_session_id)
        logging.info(obj.id)
        del request.session['checkout_session_id'] 
    else:
        logging.error(f"Check session id does not exist.")
    
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
            cleaned_data["price"]
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
        try:
            modified_stripe_price_id = utils.edit_stripe(obj, cleaned_data["title"],cleaned_data["price"])
            if not modified_stripe_price_id == "":
                updated_sub_form = form.save(commit=False)
                updated_sub_form.stripe_price_id = modified_stripe_price_id
                updated_sub_form.save()
            else:
                form.save()
            messages.success(request, "Subscription successfully updated.")
        except Exception as e:
            messages.error(request, f"Error updating subscription: {e}")
        return redirect("subscriptions:subscription_products")

    return render(request, template_name, {"form": form, "type": "edit", "obj": obj})


@role_required(allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value])
def subscription_products(request):
    utils.expire_subscriptions()
    template_name = "subscription_products/subscription_products.html"
    subscription_products = models.SubscriptionProduct.objects.filter(is_active=True)
    return render(request, template_name, {"items": subscription_products,'is_grayed_out':utils.check_if_active_subscription(request)})



@role_required(allowed_roles=[RoleEnum.ADMIN.value, RoleEnum.CANDIDATE.value])
def subscribe(request, product_id):
    user_id = request.user.id
    obj = get_object_or_404(models.SubscriptionProduct, id=product_id)
    success_path = reverse("subscriptions:success", kwargs={'sub_id':obj.id})
    cancel_path = reverse("subscriptions:cancel")
    success_url = f"{BASE_URL}{success_path}"
    cancel_url = f"{BASE_URL}{cancel_path}"
    checkout_session = stripe.checkout.Session.create(
        line_items=[{"price": obj.stripe_price_id, "quantity": 1}],
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url,
    )
    checkout_session_id = checkout_session.id
    new_sub = utils.create_subscription(obj,user_id,checkout_session_id)
    logging.info(new_sub.id)
    if new_sub.id:
        request.session['checkout_session_id'] = checkout_session_id

    return HttpResponseRedirect(checkout_session.url)
