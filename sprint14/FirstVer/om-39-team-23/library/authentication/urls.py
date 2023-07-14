from django.urls import  path
from . import views
app_name='authentication'
urlpatterns = [

    path('', views.signin,name="signin"),
    path('main/', views.main,name="main"),
    path('registration/', views.registration,name="registration"),
    path('',views.exit,name="exit"),
    path('users/',views.users,name="users"),
    path('user/<int:id>',views.get_user,name="get_user")


]