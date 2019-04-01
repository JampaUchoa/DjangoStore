from django.urls import path

from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('register/', views.client_register, name='register'),
    #path('add/<int:product_id>/', views.add_to_cart),
    #path('orders/', views.orders),
    #path('finalize/<int:order_id>/', views.finalize_order),
]