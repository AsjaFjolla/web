
from django.urls import path
from .import views
urlpatterns =  [
    path("",views.home,name="homepage"),
 path("contact/",views.contact,name= "contactpage"),
 path("detail/<id>",views.detail,name="detailpage",),
 path("register/",views.register,name="registerpage"),
#  Ketu duhet te vendoset id
 path("category/<id>",views.category,name="categorypage"),
 path()
]

