"""Defines URL patterns for author."""
from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    # Home page
    path('', views.all_authors,name='all_authors'),
    path('create/', views.create,name="create"),

    path("delete/<int:id>/", views.delete, name = 'author'),
]
