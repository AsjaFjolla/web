from django.shortcuts import render
from.models import *

# Create your views here.
def home(request):
    books=Book.objects.all()
    # Kete instruksion duhet ta vendosesh tek te gjithe funksionet pasi kategorite jane tek navbar
    categories=Category.objects.all()
    # Ketu te dalin pjeset me t fundit
    bookShelfs = Book.objects.filter(book_shelf=True)
    detailBook=Book.objects.all()
    items = Book.objects.filter(book_jornual=True)
    # Kete elementin e context "categories":categories duhet ta vendosesh tek te gjithe funksionet
    context = {"books":books, "categories":categories,"detailBook":detailBook, "bookShelfs":bookShelfs, "items": items,}
    return render(request,"home.html",context)

    

def category (request,id):
    categories=Category.objects.all()
    # Ketu modeli duhet Category pasi informacionet doti marrim nga kategoria
    categoryBook= Category.objects.get(pk = id)
    # filtrimi ne baze te kategorise
    booksincategory = Book.objects.filter(book_category=categoryBook)
    context={ "categoryBook":categoryBook, "categories":categories, 'booksincategory':booksincategory}
    return render(request,"category.html",context)
def contact(request):
    if request.method == "POST":
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        email_name = request.POST["email"]
        comment_name = request.POST["koment"]
        Contact(contact_name = first_name,
        contact_surname= last_name,
        contact_email= email_name,
        contact_comment=comment_name).save()
    categories = Category.objects.all()
    return render(request,"contact.html",{'categories': categories})

def detail(request,id):
    detailBook= Book.objects.get(pk = id)
    categories = Category.objects.all()
    context={"detailBook":detailBook, "categories":categories}
    return render(request,"detail.html",context)
    
from .models import Category

def register(request):
    if request.method == "POST":
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        email_name = request.POST["email"]
        password_name = request.POST["password"]
        Register(register_name=first_name,
                 register_surname=last_name,
                 register_email=email_name,
                 register_password=password_name).save()
    
    categories = Category.objects.all()
    return render(request, "register.html", {'categories': categories})

def best(request, id):
    best=Bestselling.objects.get(pk=id)
    best=Book.objects.filter(book_shelf=True)
    context={"best": best}
    return render(request, 'bestselling.html',context)

def item(request, id):
    item=Item.objects.get(pk=id)
    item=Book.objects.filter(book_jornual=True)
    context={"item": item}
    return render(request, 'item.html',context)


