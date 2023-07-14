from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.order_get, name='order_info'),
    path('close_order/<int:id>', views.order_close_id, name='order_close_id'),
    path('close_order/', views.order_close, name='order_close'),
    path('open_order/', views.order_open, name='order_open'),
    path('find/', views.order_find, name='order_find'),

]