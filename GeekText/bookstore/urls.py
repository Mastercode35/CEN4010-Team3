from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    
    #Home Page
    path('', views.index, name='index'),
    #Login Page
    path('login', views.login, name = 'login'),
    #Individual Book Pages
    path('books/book_info/<book_id>', views.book_info, name = "Book Info"),
    #Book Search for Top Sellers
    path('books/top', views.book_search_top, name='Book Search Top Sellers'),
    #Book Search by Genre and Sorting Factor
    path('books/<books_page>/<genre>/<sort>', views.genre_search_sort, name='Genre Search and Sort'),
    #Book Reviews Page
    path('book_review/<book_id>', views.rate_review, name='Rate and Review Book'),
    #Book review field
    path('book/<book_id>/review/<username>', views.rate_review_field, name='Review Field'),
]