from django.contrib import admin
from django.urls import include,path
from . import views


urlpatterns = [
    path('', views.log_func, name="user_get"),
    path('reg_user/', views.reg_func_user),
    path('reg_librarian/', views.reg_func_librarian),
]