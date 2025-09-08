from django.shortcuts import render
from .models import ArtModel
from .forms import *

# Create your views here.
def home_view(request):
    return render(request, 'artApp/home.html')

def landing_view(request):
    return render(request, 'artApp/base.html')

def about_view(request):
    return render(request, 'artApp/about.html')

def contact_view(request):
    return render(request, 'artApp/contact.html')

def login_view(request):
    form = UserRegistrationForm(request.Post)
    if form.is_valid:
        form.save()
    context = {
        'form':form 
    }
    return render(request, 'artApp/login.html', context)

def signup_view(request):
    form = UserRegistrationForm(request.Post)
    if form.is_valid:
        form.save()
    context = {
        'form':form 
    }
    
    """
    used to render items from the db to the template.
    obj = ArtModel.objects.get(id)
    context = {
        'object': obj
    }
    
    """
    return render(request, 'artApp/signup.html', context)

def gallery_view(request):
    return render(request, 'artApp/gallery.html')