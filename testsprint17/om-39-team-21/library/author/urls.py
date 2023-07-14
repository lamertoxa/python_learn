from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.author_get, name='author_info'),
    path('create/', views.author_form, name='author_form'),
    path('update/<int:id>', views.author_form, name='author_form'),
    path('delete/<int:id>', views.author_delete_id, name='author_delete_id'),
]