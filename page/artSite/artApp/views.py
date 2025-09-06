from django.shortcuts import render
from .models import ArtModel
from .forms import *

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'artApp/home.html')

def landing_view(request, *args, **kwargs):
    return render(request, 'artApp/base.html')

def about_view(request, *args, **kwargs):
    return render(request, 'artApp/about.html')

def contact_view(request, *args, **kwargs):
    return render(request, 'artApp/contact.html')

def login_view(request, *args, **kwargs):
    form = UserRegistrationForm(request.Post)
    if form.is_valid:
        form.save()
    context = {
        'form':form 
    }
    return render(request, 'artApp/login.html', context)

def signup_view(request, *args, **kwargs):
    obj = ArtModel.objects.get(id)
    context = {
        'object': obj
    }
    return render(request, 'artApp/signup.html')

def gallery_view(request, *args, **kwargs):
    obj = ArtModel.objects.get(id)
    context = {
        'object': obj
    }
    return render(request, 'artApp/gallery.html', context) 