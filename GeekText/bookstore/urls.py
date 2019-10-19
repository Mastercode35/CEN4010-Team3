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
    
]