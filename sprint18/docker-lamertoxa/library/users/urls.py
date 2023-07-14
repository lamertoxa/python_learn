
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.get_all_users, name='users'),
    path('<int:id>', views.user_get_one, name="user_get_one"),

]
