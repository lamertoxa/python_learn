from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.order_get, name='order_info'),
    path('close_order/<int:id>', views.order_close_id, name='order_close_id'),
    path('form/', views.order_form, name='order_form'),
    path('form/<int:id>', views.order_form, name='order_form'),

]