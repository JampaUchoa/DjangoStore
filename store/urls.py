from django.urls import path

from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('register/', views.client_register, name='register'),
    path('orders/', views.orders, name='orders'),
    path('add/<int:product_id>/', views.add_to_cart, name="add"),
    path('checkout/', views.checkout, name="checkout"),
]