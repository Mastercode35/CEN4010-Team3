from django.contrib import admin
from django.db import models

# Register your models here.
from .models import *

class CustomerDisplay(admin.ModelAdmin):
    model = Customer
    list_display = ('username', 'password', 'first_name', 'last_name', 'nickname', 'email', 'email_secondary')

class BookDisplay(admin.ModelAdmin):
    model = Book
    list_display = ('isbn', 'book_title', 'price', 'rating')

class AuthorDisplay(admin.ModelAdmin):
    model = Author
    list_display = ('first_name', 'last_name')

class InventoryDisplay(admin.ModelAdmin):
    model = Inventory
    list_display = ('book_id', 'quantity_on_hand')


admin.site.register(Customer, CustomerDisplay)
admin.site.register(Book, BookDisplay)
admin.site.register(Author, AuthorDisplay)
admin.site.register(Inventory, InventoryDisplay)