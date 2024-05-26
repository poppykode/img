from django.urls import path
from . import views

app_name = 'subscriptions'

urlpatterns = [
    path('success/<int:sub_id>/', views.success,name='success'),
    path('cancel/', views.cancel,name='cancel'),
    path('subscription-products/', views.subscription_products,name='subscription_products'),
    path('create-subscription-product/', views.create_subscription_product,name='create_subscription_product'),
    path('edit-subscription-product/<int:product_id>/', views.edit_subscription_product,name='edit_subscription_product'),
    path('subscribe/<int:product_id>/', views.subscribe,name='subscribe'),
    
]