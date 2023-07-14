from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.book_get, name='book_get'),
    path('<int:id>', views.book_get_one, name='book_get_one'),
    path('create/', views.book_form, name='book_form'),
    path('update/<int:id>', views.book_form, name='book_form'),
    path('add_author/<int:id>', views.book_author, name='book_author'),
]