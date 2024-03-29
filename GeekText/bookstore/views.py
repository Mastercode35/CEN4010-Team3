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
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .models import Customer
from django.core.exceptions import ValidationError
from django.http import HttpResponseNotFound, Http404,  HttpResponseRedirect


#Model Imports for Database Extraction
from .models import Book ,Genre,CommentRating, ShoppingCart, CreditCard, Address, Sale, SaleItem

def feed(request):
    posts = Book.objects.all()
    return render(request, 'feed.xml', {'posts': posts})

#This function will render the book_info
#
#
# page for individual books
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
    
    #If Sort by Book Title Ascending
    if sort == 'Title':
        temp = temp + "Order By b.book_title"
    #If Sort by Book Title Descending 
    if sort == 'TitleDesc':
        temp = temp + "Order By b.book_title DESC"
    #If Sort by book author name (last name ascending)
    elif sort == 'Author':
        temp = temp + "Order By a.last_name"
    #If Sort by book author name (last name descendning)
    elif sort == 'AuthorDesc':
        temp = temp + "Order By a.last_name DESC"
    #If Sort by Price (Least to Greatest)
    elif sort == 'PriceAsc':
        temp = temp + "Order By b.price"
    #If Sort by Price (Greatest to Least)
    elif sort == 'PriceDesc':
        temp = temp + "Order By b.price DESC"
    #If sort by Rating (Highest to Lowest)
    elif sort == 'Rating':
        temp = temp + "Order By b.rating DESC"
    #If sort by Rating (Lowest to Highest)
    elif sort == 'RatingAsc':
        temp = temp + "Order By b.rating"
    #If sort by Date Published
    elif sort == 'PublishDate':
        temp = temp + "Order By b.publish_date"
    #If sort by Date Published
    elif sort == 'PublishDateDesc':
        temp = temp + "Order By b.publish_date DESC"

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
    username=request.user 
    #username="guest" # for demo purposes
    bought=False
    loggedin = True
    saleitem= SaleItem.objects.raw(
         'SELECT * FROM bookstore_saleitem WHERE (book_id={0})'.format(book_id)
         )
    for s in saleitem:
        usr=s.sale.username.username
        if usr==username:
            bought=True;

    
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



def create_sale(request):

    if request.method == 'SALE':
        if request.SALE.get('submit'):
            card = CreditCard()
            card.card_number = request.SALE['card_num']
            card.expiration_date = request.SALE['ex_date']
            if request.SALE['primary']:
                card.primary_flag = True
            else: card.primary_flag = False
            card.save()

            delivery_address = Address()
            delivery_address.city = request.SALE['city']
            delivery_address.state = request.SALE['state']
            delivery_address.zip_code = request.SALE['zip']
            delivery_address.street = request.SALE['street']
            delivery_address.street_secondary = request.SALE['street2']
            delivery_address.country = request.SALE['country']
            delivery_address.address_type = request.SALE['address_type']
            delivery_address.apt = request.SALE['apt']
            delivery_address.username = (request.SALE['f_name'] + ' ' + request.SALE['l_name'])
            delivery_address.save()

            sale = Sale()
            sale.delivery_address = delivery_address
            sale.card_used = card
            sale.sale_total = request.SALE['TOTAL']
            sale.username = request.user.username
            sale.save()

            user = request.user
            user_cart = ShoppingCart.objects.raw("SELECT * FROM bookstore_shoppingcart c, bookstore_book b WHERE (c.username_id = %s) AND (b.id = c.book_id)",[user.username])
            for i in user_cart:
                SALE_ITEM = SaleItem()
                SALE_ITEM.sale = sale
                SALE_ITEM.book = i
                SALE_ITEM.quantity = i.quantity
                SALE_ITEM.save()
    return render(
        request,
        'bookstore/index.html',
        {



            'title': 'submit',
            'year': datetime.now().year,
         }
    )





def cart_order(request):


    assert isinstance(request, HttpRequest)
    user = request.user
    user_cart = ShoppingCart.objects.raw("SELECT * FROM bookstore_shoppingcart c, bookstore_book b WHERE (c.username_id = %s) AND (b.id = c.book_id)", [user.username])
    length = len(user_cart)
    total_price = 0

    for i in user_cart:

        total_price = total_price + (i.price * i.quantity)




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

def SignUp(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect("/login/login/")
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'bookstore/signup.html', {'form': f})

