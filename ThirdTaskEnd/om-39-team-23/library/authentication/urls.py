from django.urls import  path
from . import views
app_name='authentication'
urlpatterns = [
    path('',views.start_page,name='start_page'),
    path('signin', views.signin,name="signin"),
    path('main/', views.main,name="main"),
    path('registration/', views.registration,name="registration"),
    path('exit/',views.exit,name="exit"),
    path('users/',views.users,name="users"),
    path('user/<int:id>',views.get_user,name="get_user")


]