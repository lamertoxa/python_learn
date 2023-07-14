from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.author_get, name='author_info'),
    path('new/', views.author_new, name='author_new'),
    path('delete/', views.author_delete, name='author_delete'),
    path('delete/<int:id>', views.author_delete_id, name='author_delete_id'),
]