from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='index'),
    path("home",views.home,name='home'),
    path("facts",views.facts,name='facts'),
    path("products",views.products,name='products'),
    path("contact",views.contact,name='contact'),
    path("login",views.login,name='login')
]
