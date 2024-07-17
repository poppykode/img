from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages
from datetime import date
from subscriptions.models import Subscription

def role_required(allowed_roles=[]):
  def decorator(view_func):
    @login_required
    def wrapper(request, *args, **kwargs):
      if not request.user.is_authenticated:
        return login_required(view_func)(request, *args, **kwargs)      
      if not allowed_roles:
        return view_func(request, *args, **kwargs)     
      for role in allowed_roles:
        if request.user.role == role:      
            return view_func(request, *args, **kwargs)
        # will put redirect url

      return redirect("accounts:not_authorized")
    return wrapper
  return decorator


def subscription_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        try:
            subscription = Subscription.objects.get(user=request.user, is_active=True)
            if subscription.expiration_date and subscription.expiration_date >= date.today():
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, "Your subscription has expired. Please renew to continue.")
        except Subscription.DoesNotExist:
            messages.error(request, "You need a valid subscription to access this page.")
        
        return redirect('subscriptions:subscription_products')

    return _wrapped_view_func
