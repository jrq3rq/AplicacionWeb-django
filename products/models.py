from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Specs(models.Model):
    engine = models.CharField(max_length=255)
    doors = models.CharField(max_length=255)
    motor = models.FloatField()
    layout = models.CharField(max_length=255)

