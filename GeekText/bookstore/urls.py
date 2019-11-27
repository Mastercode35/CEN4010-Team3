from django.contrib.auth.views import *
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    
    #Home Page
    path('', views.index, name='index'),
    #Login Page
    path('login/', include('django.contrib.auth.urls')),
    #SignUp
    path('signup/', views.SignUp, name='signup'),
    #Individual Book Pages
    path('bookstore/book_info/<book_id>', views.book_info, name = "Book Info"),
    #Book Search for Top Sellers
    path('books/top', views.book_search_top, name='Book Search Top Sellers'),
    #Book Search by Genre and Sorting Factor
    path('books/<books_page>/<genre>/<sort>', views.genre_search_sort, name='Genre Search and Sort'),
    #Book Reviews Page
    path('book/<book_id>/<review>', views.rate_review_field, name='Review Field'),
    #Shopping Cart
    path('shopping_cart', views.cart_order, name='Shopping Cart'),
    url('shopping_cart', views.create_sale, name="submit")

]
