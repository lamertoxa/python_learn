from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.book_get, name='book_info'),
    path('<int:id>', views.book_get_one, name='book_get_one'),
    path('<int:id>/<str:change>/', views.book_get_one, name='book_change_one'),
    path('find/', views.book_find, name='book_find'),
    path('book_find_id/', views.book_id_find, name='book_find_id')

]