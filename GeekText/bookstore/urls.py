from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    
    #Home Page
    path('', views.index, name='index'),
    #Login Page
    path('login', views.login, name = 'login'),
    #Book Search Page
    path('books', views.book_search, name='Book Search'),
    #Book Search for Top Sellers
    path('books/top', views.book_search_top, name='Book Search Top Sellers'),
    #Book Search by Genre
    path('books/<genre>', views.genre_search, name='Genre Search'),
    #Book Search by Genre and Sort
    path('books/<genre>/<sort>', views.genre_search_sort, name='Genre Search and Sort'),
    
]