from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('gallery/', gallery_view),
    path('signup/', signup_view),
    path('home/', home_view),
    path('nav/', nav_view)
]
