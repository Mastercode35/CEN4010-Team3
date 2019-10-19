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
            'SELECT * FROM bookstore_book b, bookstore_wrote w, bookstore_author a WHERE (w.author_id = a.id) AND (w.book_id = b.id)'
        )

    genre_list = Genre.objects.raw(
            'SELECT * FROM bookstore_genre'
    )

    return render(request, 'bookstore/book_search.html', 
        {'books': books_list,
         'genres': genre_list,
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



