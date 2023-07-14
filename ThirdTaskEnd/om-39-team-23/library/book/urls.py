from django.urls import  path
from . import views
app_name='book'
urlpatterns = [

    path('', views.all_books,name="all_books"),
    path('about_book/<int:id>/', views.get_book,name="get_book"),
    path('search_book/', views.search_book,name="search_book"),

]