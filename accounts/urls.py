from django.urls import path
from .views import (auth,dashboard,applications) 

app_name = 'accounts'

urlpatterns = [
    path('login',auth.login, name='login'),
    path('',auth.redirect_logged, name='redirect_logged'),
    path('not-authorized-404',auth.not_authorized, name='not_authorized'),
    path('logout',auth.my_logout, name='logout'),

    path('dashboard/admin/',dashboard.admin_dashboard, name='admin_dashboard'),
    path('dashboard/candidate/',dashboard.candidate_dashboard, name='candidate_dashboard'),
    path('dashboard/coach',dashboard.coach_dashboard, name='coach_dashboard'),
    path('profile',dashboard.profile, name='profile'),
    path('public-profile/<uuid:user_id>',dashboard.public_profile,name='public_profile'),
    path('users',dashboard.users, name='users'),
    path('admin-profile/<uuid:coach_id>',dashboard.admin_profile, name='admin_profile'),
    path('activate-or-deactivate_account/<uuid:user_id>',dashboard.activate_or_deactivate_account, name='activate_or_deactivate_account'),
    path('add-admin',dashboard.add_admin, name='add_admin'),
    path('change-password',dashboard.change_password, name='change_password'),
    path('upload-profile-picture',dashboard.upload_profile_picture, name='upload_profile_picture'),
    path('update-personal-details',dashboard.update_personal_details, name='update_personal_details'),
    path('update-general-additional-info',dashboard.update_general_additional_info, name='update_general_additional_info'),
    path('update-exam-date',dashboard.update_exam_date, name='update_exam_date'),

    path('register-study-buddy',auth.StudyBuddyDataWizard.as_view(),name='register_study_buddy')
]