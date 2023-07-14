from django.urls import  path
from . import views
app_name='order'
urlpatterns = [

    path('', views.all_orders,name="all_orders"),
    path('my_orders/', views.my_orders,name="my_orders"),
    path('new_orders/', views.new_orders,name="new_orders"),


]