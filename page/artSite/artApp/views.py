from django.shortcuts import render
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'artApp/home.html')

def landing_view(request, *args, **kwargs):
    return render(request, 'artApp/base.html')

def nav_view(request, *args, **kwargs):
    return render(request, 'artApp/nav.html')

def about_view(request, *args, **kwargs):
    return render(request, 'artApp/about.html')

def contact_view(request, *args, **kwargs):
    return render(request, 'artApp/contact.html')

def login_view(request, *args, **kwargs):
    return render(request, 'artApp/login.html')

def signup_view(request, *args, **kwargs):
    return render(request, 'artApp/signup.html')

def gallery_view(request, *args, **kwargs):
    return render(request, 'artApp/gallery.html') 