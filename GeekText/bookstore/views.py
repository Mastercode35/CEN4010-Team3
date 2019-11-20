import math
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
from .models import Book ,Genre,CommentRating, ShoppingCart, CreditCard, Address, Sale,SaleItem

def feed(request):
    posts = Book.objects.all()
    return render(request, 'feed.xml', {'posts': posts})

def book_search_top(request):
    books_list = Book.objects.raw(
            'SELECT * FROM bookstore_book b, bookstore_wrote w, bookstore_author a WHERE (w.author_id = a.id) AND (w.book_id = b.id) AND (w.sequence = 1) ORDER BY b.sales_rank LIMIT 10'
        )

    genre_list = Genre.objects.raw(
            'SELECT * FROM bookstore_genre'
    )

    books = []
    temp = []

    for book in books_list:
        if len(temp) == 3:
            books.append(temp)
            temp = []
        
        temp.append(book)

    books.append(temp)

    return render(request, 'bookstore/book_search.html', 
        {'books': books,
         'genres': genre_list,
         'title':'Book Search Page',
         'top': True,
         'year':datetime.now().year,}
    )

#This function will render the book_info page for individual books
def book_info(request, book_id):
     book=Book.objects.raw(
            'SELECT * FROM bookstore_book b, bookstore_wrote w, bookstore_author a WHERE (w.author_id = a.id) AND (w.book_id = b.id) AND (w.sequence = 1) AND (b.id ={0})'.format(book_id)
        )
     info= Book.objects.raw(
            'SELECT * FROM bookstore_book WHERE(id ={0})'.format(book_id) 
         )

     return render (request,'bookstore/learnmore.html',
        {  'book': book,
           'info':info,
           'title':'Book Info Page',
           'year':datetime.now().year}   
     )


def genre_search_sort(request, books_page, genre, sort):

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

    parts = books_page.split('-')
    bpp = int(parts[0])
    page = int(parts[1])

    limit_start = bpp * (page - 1)

    all_books = Book.objects.raw('{0}'.format(temp))

    #Add the LIMIT and OFFSET keywords to limit for pagination
    temp = temp + " LIMIT {0} OFFSET {1}".format(bpp, limit_start)

    #This query grabs all the books needed to display
    books_list = Book.objects.raw(
        '{0}'.format(temp)
    )

    
    #Grab the total number of books to figure out how many total pages are possible to display
    total_books = len(all_books)
    total_pages =  math.ceil(total_books / bpp)
    first_page = False
    last_page = False

    if page == 1:
        first_page == True
    if page == total_pages:
        last_page == True


    #Make the query for all the genres
    genre_list = Genre.objects.raw(
            'SELECT * FROM bookstore_genre'
    )

    books = []
    temp = []

    for book in books_list:
        if len(temp) == 3:
            books.append(temp)
            temp = []
        
        temp.append(book)

    books.append(temp)

    return render(request, 'bookstore/book_search.html', 
        {'books': books,
         'genres': genre_list,
         'genre':genre,
         'sort': sort,
         'bpp': bpp,
         'page': page,
         'first_page': first_page,
         'last_page': last_page,
         'current_page': page,
         'total_pages': total_pages,
         'total_books': total_books,
         'title':'Book Search Page',
         'year':datetime.now().year,}
    )




def rate_review_field(request,book_id,review):
    
    book=Book.objects.raw(
            'SELECT * FROM bookstore_book b, bookstore_wrote w, bookstore_author a WHERE (w.author_id = a.id) AND (w.book_id = b.id) AND (w.sequence = 1) AND (b.id ={0})'.format(book_id)
        )
    username="guest"
    bought=False
    loggedin = True
    sale= Sale.objects.raw(
         'SELECT s.id FROM bookstore_saleitem si, bookstore_sale s WHERE (si.book_id={0}) AND (si.sale_id=s.id)'.format(book_id)
         )
    for s in sale:
        
        u=(s.username.username)
        
        if u==username:  
            print("%s",u)
            bought=True

    
    if bought:
        if request.method == 'POST':
            user_select=request.POST['userid']
            rate= request.POST['rating']
            msg=request.POST['review_message_field']

            b1=CommentRating(comment=msg,rating=rate,book_id=book_id, username_id=user_select)
            b1.save()
       
    comments= CommentRating.objects.raw(
         'SELECT * FROM bookstore_commentrating bc WHERE (bc.book_id={0})'.format(book_id)
         )
    return render(request, 'bookstore/book_review.html', 
    {   'book': book,
        'username': username,
        'bought':bought,
        'comments':comments,
        'loggedin':loggedin,
        'title':'Book Review Page',
        'review': review,
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

def cart_order(request):


    assert isinstance(request, HttpRequest)

    user_cart = ShoppingCart.objects.raw("SELECT * FROM bookstore_shoppingcart c, bookstore_book b WHERE (c.username_id = 'guest') AND (b.id = c.book_id)")
    length = len(user_cart)
    total_price = 0

    for i in user_cart:

        total_price = total_price + i.price


    return render(
    request,
    'bookstore/shopping_cart.html',
    {
        'cart': user_cart,

        'total': total_price,
        'title': 'Shopping Cart',
        'year': datetime.now().year,
    }
    )

def create_sale(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'SALE':
        if request.SALE.get('card_num') and request.SALE.get('ex_date') and request.SALE.get('security_code') and request.SALE.get('f_name') and request.SALE.get('l_name') and request.SALE.get('street') and request.SALE.get('state'):
            card = CreditCard()
            card.card_number = request.SALE.get('card_num')
            card.expiration_date = request.SALE.get('ex_date')
            if request.SALE.get('primary'):
                card.primary_flag = True
            else: card.primary_flag = False
            card.save()

            delivery_address = Address()
            delivery_address.city = request.SALE.get('city')
            delivery_address.state = request.SALE.get('state')
            delivery_address.zip_code = request.SALE.get('zip')
            delivery_address.street = request.SALE.get('street')
            delivery_address.street_secondary = request.SALE.get('street2')
            delivery_address.country = request.SALE.get('country')
            delivery_address.address_type = request.SALE.get('address_type')
            delivery_address.apt = request.SALE.get('apt')
            delivery_address.username = 'guest'
            delivery_address.save()

            sale = Sale()
            sale.delivery_address = delivery_address
            sale.card_used = card
            sale.sale_total = request.SALE.get('TOTAL')
            sale.username = 'guest'
            sale.save()

    return render(
        request,
        'bookstore/shopping_cart.html',
        {

            'title': 'Shopping Cart',
            'year': datetime.now().year,
        }
    )



