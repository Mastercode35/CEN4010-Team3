from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'login', views.login),
    url(r'', views.index, name='index'),
    url(r'books', views.book_search, name='Book Search'),
    
]