from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.order_list, name='order-list'),
    path('add/', views.add_order, name='add-order'),
]

