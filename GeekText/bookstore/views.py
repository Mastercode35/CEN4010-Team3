from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

def feed(request):
    posts = Book.objects.all()
    return render(request, 'feed.xml', {'posts': posts})

def index(request):
    return HttpResponse("Hello, you are viewing the BookStore index.")
