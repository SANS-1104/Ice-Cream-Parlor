from django.shortcuts import render, HttpResponse
from home.models import Contact, Login

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home (request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')

def facts (request):
    return render(request, 'facts.html')

def contact (request):
    if request.method == "POST":
        enquiry = request.POST.get('enquiry')
        contact = Contact(enquiry = enquiry)
        contact.save()
    return render(request, 'contact.html')

def login (request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        yes = request.POST.get('yes')

        login = Login(fname=fname, lname = lname, email = email, phone = phone, yes = True)
        login.save()
        messages.success(request, "Form Submitted Successfully !!")

    return render(request, 'login.html')
