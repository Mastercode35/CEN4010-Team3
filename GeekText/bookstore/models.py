from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length = 25, primary_key = True)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    nickname = models.CharField(max_length = 25)
    email = models.CharField(max_length = 50)
    email_secondary = models.CharField(max_length = 50, blank = True)
    password = models.CharField(max_length = 25)
    start_date = models.DateField(auto_now_add = True)

class Addresses(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "user address is associated to")
    address_street = models.CharField(max_length = 25)
    address_street_secondary = models.CharField(max_length = 25, blank = True)
    address_apt = models.CharField(max_length = 10, blank = True)
    address_city = models.CharField(max_length = 15)
    address_state = models.CharField(max_length = 15)
    address_zip = models.IntegerField()
    address_country = models.CharField(max_length = 25)
    address_type = models.CharField(max_length = 25)

class CreditCards(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "customer card is related to")
    card_number = models.IntegerField()
    expiration_date = models.DateField()
    primary_flag = models.BooleanField()

class Publisher(models.Model):
    publisher_name = models.CharField(max_length = 50)

class Genre(models.Model):
    genre = models.CharField(max_length = 50)

class Book(models.Model):
    isbn = models.IntegerField()
    book_title = models.CharField(max_length = 100)
    book_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name = "book genre")
    book_description = models.CharField(max_length = 1000, blank = True)
    publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name = "publisher")
    image_url = models.CharField(max_length = 200, blank = True)
    file_path = models.CharField(max_length = 200, blank = True)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)
    rating = models.DecimalField(max_digits = 1, decimal_places = 1)

class Comments_Ratings(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name = "book comment/rating is for")
    username = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 1000)
    rating = models.DecimalField(max_digits=1, decimal_places = 1)

class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

class Wrote(models.Model):
    Book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    sequence = models.IntegerField()

class Inventory(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity_on_hand = models.IntegerField()

class ShoppingCart(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "user cart assosiated to")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name = "book in cart")
    quantity = models.IntegerField()

class WishList(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "user list assosiated to")
    list_name = models.CharField(max_length = 50)
    primary_list = models.BooleanField()

class WishListItems(models.Model):
    list_id = models.ForeignKey(WishList, on_delete=models.CASCADE, verbose_name = "wish list associated with this item")
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "user list is assosiated to")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name = "book in list")

class SavedForLater(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name = "user item is assosiated to")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name = "book in list")

class Sales(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField(auto_now_add = True)
    delivery_address = models.ForeignKey(Addresses, on_delete = models.CASCADE)
    card_used = models.ForeignKey(CreditCards, on_delete = models.CASCADE)
    sale_total = models.DecimalField(max_digits = 4, decimal_places = 2)

class SaleItems(models.Model):
    sale_id = models.ForeignKey(Sales, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
