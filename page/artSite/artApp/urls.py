from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_view),
    path('About/', about_view, name = 'about'),
    path('Contact/', contact_view, name='contact'),
    path('gallery/', gallery_view, name = 'gallery'),
    path('Home/', home_view, name = 'home'),
]
