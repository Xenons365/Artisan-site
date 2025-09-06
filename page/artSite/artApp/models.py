from django.db import models

# Create your models here.
class ArtModel(models.Model):
    email = models.EmailField(max_length=254, blank='False')
    password = models.CharField(max_length=50, blank='False')