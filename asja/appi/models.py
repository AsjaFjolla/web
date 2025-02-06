from django.db import models

# Create your models here.

class Category(models.Model):
    category_title=models.CharField(max_length=250,null=250,blank=True)
    def __str__(self):
     return f"{self.category_title}"


class Bestselling(models.Model):
   best_title=models.CharField(max_length=250,blank=True)
   best_image=models.ImageField(upload_to="item/",null=True,blank=True)
   best_description=models.TextField(max_length=500,null=True,blank=True)
   best_price=models.DecimalField(max_digits=5,decimal_places=3,null=True,blank=True)


class Item(models.Model):
    item_title = models.CharField(max_length=250,null=True, blank=True)
    item_image = models.ImageField(upload_to="best/", null=True, blank=True )
    item_description=models.TextField(max_length=500,null=True,blank=True)
    item_price=models.DecimalField(max_digits=5,decimal_places=3,null=True,blank=True)
   
    

class Book(models.Model):
    book_title=models.CharField(max_length=250,null=250,blank=True)
    book_description=models.TextField(max_length=2000,null=True,blank=True)
    book_image=models.ImageField(upload_to="book/",null=True,blank=True)
    book_price=models.DecimalField(max_digits=5,decimal_places=3,null=True,blank=True)
    book_category=models.ForeignKey(Category, null= True, blank=True, on_delete=models.CASCADE)
    book_shelf=models.BooleanField(null=True,blank=True)
    book_jornual=models.BooleanField(null=True,blank=True)
    

    #book_quantity_int=models.IntegerField(null=True,blank=True) nr e plote jo per cmimet
    #book_quantity_float=models.FloatField(null=True,blank=True) nr me presje

    def __str__(self):
     return f"{self.book_title}"
    
    

    
class Contact(models.Model):
    contact_name=models.CharField(max_length=250,null=True,blank=True)
    contact_surname=models.CharField(max_length=250,null=True,blank=True)
    contact_email=models.EmailField(null=True,blank=True)
    contact_comment=models.TextField(max_length=250,null=True,blank=True)

    
    
    def __str__(self):
        return f"{self.contact_name} {self.contact_surname}"
    
class Register(models.Model):
    register_name=models.CharField(max_length=250,null=True,blank=True)
    register_surname=models.CharField(max_length=250,null=True,blank=True)
    register_email=models.EmailField(null=True,blank=True)
    register_password=models.TextField(max_length=250,null=True,blank=True)

    def __str__(self):
        return f"{self.register_name} {self.register_surname}"

