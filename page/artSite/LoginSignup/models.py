from django.db import models
from django import forms

# Create your models here.

class LoginModel(models.Model):
    email = models.EmailField(max_length=254, blank='False')
    password = models.CharField(max_length=50, blank='False')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")