from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_view),
    path('about.html/', about_view),
    path('contact.html/', contact_view),
    path('gallery.html/', gallery_view),
    path('signup.html/', signup_view),
    path('home.html/', home_view),
    
]
