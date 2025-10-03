from django.urls import path, include
from .views import *

urlpatterns = [
    path('About/', about_view, name = 'about'),
    path('Contact/', contact_view, name='contact'),
    path('gallery/', gallery_view, name = 'gallery'),
    path('shop/', shop_view, name = 'shopping'),
    path('', home_view, name = 'home'),
]
