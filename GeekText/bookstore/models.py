from django.db import models

# Create your models here.

#Customer Table which contains all the information a Customer needs for our site
class Customer(models.Model):
    username = models.CharField(max_length = 25, primary_key = True)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    nickname = models.CharField(max_length = 25)
    email = models.CharField(max_length = 50)
    email_secondary = models.CharField(max_length = 50, blank = True)
    password = models.CharField(max_length = 25)
    start_date = models.DateField(auto_now_add = True)

#Addresses Table which contains all addresses used by 'username'
#Uses primarily Customer as a Foreign Key Table
class Address(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "user address is associated to")
    street = models.CharField(max_length = 25)
    street_secondary = models.CharField(max_length = 25, blank = True)
    apt = models.CharField(max_length = 10, blank = True)
    city = models.CharField(max_length = 15)
    state = models.CharField(max_length = 15)
    zip_code = models.IntegerField()
    country = models.CharField(max_length = 25)
    address_type = models.CharField(max_length = 25)

#CreditCards Table which contains all credit cards used by 'username'
#Uses primarily Customer as a Foreign Key Table
class CreditCard(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "customer card is related to")
    card_number = models.IntegerField()
    expiration_date = models.DateField()
    primary_flag = models.BooleanField()

#Publisher Table
class Publisher(models.Model):
    publisher_name = models.CharField(max_length = 50)

#Genre Table
class Genre(models.Model):
    genre = models.CharField(max_length = 50)

#Book Table which contains all the information needed for book.
#Foreign Key Tables: Genre, Publisher
class Book(models.Model):
    isbn = models.CharField(max_length = 15)
    book_title = models.CharField(max_length = 100)
    book_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name = "book genre")
    book_description = models.CharField(max_length = 2000, blank = True)
    publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name = "publisher")
    publish_date = models.DateField()
    image_url = models.CharField(max_length = 200, blank = True)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)
    rating = models.DecimalField(max_digits = 2, decimal_places = 1)
    sales_rank = models.IntegerField()

#Comments and Ratings table which contain all the comments with their ratings for each book in Book that have comments/ratings
#Foreign Key Tables: Book (Book being commented) and Customer (user doing the commenting)
class CommentRating(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name = "book comment/rating is for")
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "customer doing the rating/commenting")
    comment = models.CharField(max_length = 2000)
    rating = models.DecimalField(max_digits=2, decimal_places = 1)

#Author Table
class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

#Wrote Table
#Connects Each author in the DB with the books they wrote.
#Foreign Key Tables: Book (book written by an author) and Author (author doing the writing)
class Wrote(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    sequence = models.IntegerField()

#Inventory Table - Connects each book with how many we have in the store.
#Foreign Key Tables: Book (book being counted)
class Inventory(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity_on_hand = models.IntegerField()

#Shopping Cart Table which contains the items in each shopping cart and which user they are owned by
#Foreign Key Tables: Customer (user who owns the cart) and Book (book within that cart.)
class ShoppingCart(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "user cart assosiated to")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name = "book in cart")
    quantity = models.IntegerField()

#Wish List Table which contains the names of each wish list and the user who owns them
#Foreign Key Tables: Customer (user who owns the list)
class WishList(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "user list assosiated to")
    list_name = models.CharField(max_length = 50)
    primary_list = models.BooleanField()

#Wish List Items Tables which contains each book held within each wishlist
#Foreign Key Tables: WisList (the list the books are connected to) and Book (Book inside the list)
class WishListItem(models.Model):
    list_id = models.ForeignKey(WishList, on_delete=models.CASCADE, verbose_name = "wish list associated with this item")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name = "book in list")

#SavedForLater Table which holds each book that will be saved for later by each user.
#Foreign Key Tables: Customer (user saving books for later) and Book (book being saved for later)
class SavedForLater(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "user item is assosiated to")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name = "book in list")

#Sales Table which contains each sale made on the site and their necessary information.
#Foeign Key Tables: Customer (user who made the sale), Addresses (delivery address of sale), and CreditCards (card used for sale)
class Sale(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField(auto_now_add = True)
    delivery_address = models.ForeignKey(Address, on_delete = models.CASCADE)
    card_used = models.ForeignKey(CreditCard, on_delete = models.CASCADE)
    sale_total = models.DecimalField(max_digits = 4, decimal_places = 2)

#Sale Items Table which contains each book found within each sale made
#Foreign Key Tables: Sales (sale made) and Book (book sold in that sale)
class SaleItem(models.Model):
    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
