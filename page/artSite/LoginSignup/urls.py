from django.urls import path
from .views import *

urlpatterns = [
    path('Login/', login_view, name='login'),
    path('Signup/', signup_view, name='signup'),
]