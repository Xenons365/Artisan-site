from django.db import models

# Create your models here.
class ArtModel(models.Model):
    email = models.EmailField(max_length=254, blank='False')
    password = models.CharField(max_length=50, blank='False')
    title = models.CharField(max_length=250, blank='False')
    price = models.DecimalField(blank="False", max_digits=100000, decimal_places=2, null='False')
    description = models.TextField(null="True", blank= 'True')