from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

#Model Imports for Database Extraction
from django.db import connection
from .models import Book, Genre

def feed(request):
    posts = Book.objects.all()
    return render(request, 'feed.xml', {'posts': posts})

def book_search(request):
    books_list = Book.objects.raw(
            'SELECT * FROM bookstore_book b, bookstore_wrote w, bookstore_author a WHERE (w.author_id = a.id) AND (w.book_id = b.id) AND (w.sequence = 1)'
        )

    genre_list = Genre.objects.raw(
            'SELECT * FROM bookstore_genre'
    )

    return render(request, 'bookstore/book_search.html', 
        {'books': books_list,
         'genres': genre_list,
         'currnet_genre': 'All',
         'title':'Book Search Page',
         'year':datetime.now().year,}
    )

def book_search_top(request):
    books_list = Book.objects.raw(
            'SELECT * FROM bookstore_book b, bookstore_wrote w, bookstore_author a WHERE (w.author_id = a.id) AND (w.book_id = b.id) AND (w.sequence = 1) ORDER BY b.sales_rank LIMIT 10'
        )

    genre_list = Genre.objects.raw(
            'SELECT * FROM bookstore_genre'
    )

    return render(request, 'bookstore/book_search.html', 
        {'books': books_list,
         'genres': genre_list,
         'currnet_genre': 'All',
         'title':'Book Search Page',
         'top': True,
         'year':datetime.now().year,}
    )

def genre_search(request, genre):
    
    if genre == 'All':
        temp = ''
    else:
        temp = 'AND (b.book_genre_id = {})'.format(genre)

    books_list = Book.objects.raw(
        'SELECT * FROM bookstore_book b, bookstore_wrote w, bookstore_author a WHERE (w.author_id = a.id) AND (w.book_id = b.id) AND (w.sequence = 1) {}'.format(temp)
    )

    genre_list = Genre.objects.raw(
            'SELECT * FROM bookstore_genre'
    )

    return render(request, 'bookstore/book_search.html', 
        {'books': books_list,
         'genres': genre_list,
         'genre':genre,
         'title':'Book Search Page',
         'year':datetime.now().year,}
    )

def genre_search_sort(request, genre, sort):

    temp = "SELECT * FROM bookstore_book b, bookstore_wrote w, bookstore_author a WHERE (w.author_id = a.id) AND (w.book_id = b.id) AND (w.sequence = 1) "

    #Sort by different Ratings
    if sort == '1Star':
        temp = temp + 'AND (b.rating > 0.0) '
    elif sort == '2Star':
        temp = temp + 'AND (b.rating > 1.0) '
    elif sort == '3Star':
        temp = temp +  'AND (b.rating > 2.0) '
    elif sort == '4Star':
        temp = temp + 'AND (b.rating > 3.0) '
    elif sort == '5Star':
        temp = temp + 'AND (b.rating > 4.0) '

    #Keeps the genre that was previously selected
    if genre != 'All':
        temp = temp + "AND (b.book_genre_id = {0})".format(genre)
    
    #If Sort by Book Title
    if sort == 'Title':
        temp = temp + "Order By b.book_title ASC"
    #If Sort by book author name (last name)
    elif sort == 'Author':
        temp = temp + "Order By a.last_name ASC"
    #If Sort by Price (Least to Greatest)
    elif sort == 'PriceAsc':
        temp = temp + "Order By b.price ASC"
    #If Sort by Price (Greatest to Least)
    elif sort == 'PriceDesc':
        temp = temp + "Order By b.price DESC"
    #If sort by Rating (Highest to Lowest)
    elif sort == 'Rating':
        temp = temp + "Order By b.rating DESC"
    #If sort by Date Published
    elif sort == 'PublishDate':
        temp = temp + "Order By b.publish_date ASC"

    books_list = Book.objects.raw(
        '{0}'.format(temp)
    )

    genre_list = Genre.objects.raw(
            'SELECT * FROM bookstore_genre'
    )

    return render(request, 'bookstore/book_search.html', 
        {'books': books_list,
         'genres': genre_list,
         'genre':genre,
         'title':'Book Search Page',
         'year':datetime.now().year,}
    )


def login(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'bookstore/login.html',
        {
            'title':'Log in',
            'year':datetime.now().year,
        }
    )

def index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'bookstore/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )



