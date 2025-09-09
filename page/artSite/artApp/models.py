from django.db import models


# Create your models here.
class ArtModel(models.Model):
    title = models.CharField(max_length=250, blank='False')
    price = models.DecimalField(blank="False", max_digits=100000, decimal_places=2, null='False')
    description = models.TextField(null="True", blank= 'True')