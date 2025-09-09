from django.shortcuts import render
from .forms import *


# Create your views here.
def signup_view(request):
    form = UserRegistrationForm(request.Post)
    if form.is_valid:
        form.save()
    context = {
        'form':form 
    }
    return render(request, 'LoginSignup/signup.html', context)

def login_view(request):
    form = UserRegistrationForm(request.Post)
    if form.is_valid:
        form.save()
    context = {
        'form':form 
    }
    return render(request, 'LoginSignup/login.html', context)