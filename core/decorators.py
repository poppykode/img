from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

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

def check_subscription():
  pass
