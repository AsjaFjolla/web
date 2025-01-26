from django.shortcuts import render
from.models import *

# Create your views here.
def home(request):
    books=Book.objects.all()
    # Kete instruksion duhet ta vendosesh tek te gjithe funksionet pasi kategorite jane tek navbar
    categories=Category.objects.all()
    # Ketu te dalin pjeset me t fundit
    bookShelfs = Book.objects.filter(book_shelf=True)
    # Kete elementin e context "categories":categories duhet ta vendosesh tek te gjithe funksionet
    context = {"books":books, "categories":categories, "bookShelfs":bookShelfs,}
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
    return render(request,"contact.html")
def detail(request,id):
    detailBook= Book.objects.get(pk = id)
    context={"detailBook":detailBook}
    return render(request,"detail.html",context)
def register(request):
    return render(request,"register.html")

def best(request, id):
    best=Best.objects.get(pk=id)
    best=Book.objects.filter(book_shelf=True)
    context={"best": best}
    return render(request, 'bestselling.html',context)

