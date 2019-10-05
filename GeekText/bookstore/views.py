from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime



# Create your views here.

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