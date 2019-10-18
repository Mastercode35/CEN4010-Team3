from django.contrib import admin
from django.db import models

# Register your models here.
from .models import *

class CustomerDisplay(admin.ModelAdmin):
    model = Customer
    list_display = ('username', 'password', 'first_name', 'last_name', 'nickname', 'email', 'email_secondary')

class AddressDisplay(admin.ModelAdmin):
    model = Address
    list_display = ('username', 'street', 'city', 'state', 'zip_code', 'country', 'address_type')

class CardsDisplay(admin.ModelAdmin):
    model = CreditCard
    list_display = ('username', 'card_number', 'expiration_date', 'primary_flag')

class PublisherDisplay(admin.ModelAdmin):
    model = Publisher
    list_display = ['publisher_name']

class GenreDisplay(admin.ModelAdmin):
    model = Genre
    list_display = ['genre']

class BookDisplay(admin.ModelAdmin):
    model = Book
    list_display = ('isbn', 'book_title', 'book_genre', 'price', 'rating', 'sales_rank')

class CommentsDisplay(admin.ModelAdmin):
    model = CommentRating
    list_display = ('book_id', 'username', 'comment', 'rating')

class AuthorDisplay(admin.ModelAdmin):
    model = Author
    list_display = ('first_name', 'last_name')

class WroteDisplay(admin.ModelAdmin):
    model = Wrote
    list_display = ('book_id', 'author_id', 'sequence')

class InventoryDisplay(admin.ModelAdmin):
    model = Inventory
    list_display = ('book_id', 'quantity_on_hand')

class CartDisplay(admin.ModelAdmin):
    model = ShoppingCart
    list_display = ('username', 'book_id', 'quantity')

class WishDisplay(admin.ModelAdmin):
    model = WishList
    list_display = ('username', 'list_name', 'primary_list')

class WishItemsDisplay(admin.ModelAdmin):
    model = WishListItem
    list_display = ('list_id', 'book_id')

class SavedDisplay(admin.ModelAdmin):
    model = SavedForLater
    list_display = ('username', 'book_id')

class SalesDisplay(admin.ModelAdmin):
    model = Sale
    list_display = ('username', 'sale_date', 'delivery_address', 'card_used', 'sale_total')

class SaleItemsDisplay(admin.ModelAdmin):
    pasmodel = SaleItem
    list_display = ('sale_id', 'book_id', 'quantity')



admin.site.register(Customer, CustomerDisplay)
admin.site.register(Address, AddressDisplay)
admin.site.register(CreditCard, CardsDisplay)
admin.site.register(Publisher, PublisherDisplay)
admin.site.register(Genre, GenreDisplay)
admin.site.register(Book, BookDisplay)
admin.site.register(CommentRating, CommentsDisplay)
admin.site.register(Author, AuthorDisplay)
admin.site.register(Wrote, WroteDisplay)
admin.site.register(Inventory, InventoryDisplay)
admin.site.register(ShoppingCart, CartDisplay)
admin.site.register(WishList, WishDisplay)
admin.site.register(WishListItem, WishItemsDisplay)
admin.site.register(SavedForLater, SavedDisplay)
admin.site.register(Sale, SalesDisplay)
admin.site.register(SaleItem, SaleItemsDisplay)
