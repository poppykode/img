from django.urls import path
from .views import auth,dashboard,applications

app_name = 'accounts'

urlpatterns = [
    path('login',auth.login, name='login'),
    path('',auth.redirect_logged, name='redirect_logged'),
    path('not-authorized-404',auth.not_authorized, name='not_authorized'),

    path('dashboard/admin',dashboard.admin_dashboard, name='admin_dashboard'),
    path('dashboard/candidate',dashboard.candidate_dashboard, name='candidate_dashboard'),
    path('dashboard/coach',dashboard.coach_dashboard, name='coach_dashboard')
]