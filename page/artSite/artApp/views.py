from django.shortcuts import render
from .models import ArtModel

# Create your views here.
def home_view(request):
    return render(request, 'artApp/home.html')

def landing_view(request):
    return render(request, 'artApp/base.html')

def about_view(request):
    return render(request, 'artApp/about.html')

def contact_view(request):
    return render(request, 'artApp/contact.html')
 
"""

    used to render items from the db to the template.
def shop_view(request):
    obj = ArtModel.objects.get(id)
    context = {
        'object': obj
    }

    return render(request, 'artApp/gallery.html')
"""

def gallery_view(request):
    return render(request, 'artApp/gallery.html')

def shop_view(request):
    obj = ArtModel.objects.get(id)
    context = {
        'object': obj
    }

    return render(request, 'artApp/gallery.html')