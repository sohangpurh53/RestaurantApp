from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255, default='')
    detail = models.TextField(default='')
    price = models.FloatField(default='')
    image = models.URLField(default='')
    
    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=255, default='')
    message = models.TextField(default='')
    rating = models.IntegerField(default='')
    profile = models.URLField(default='')
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    name = models.CharField(max_length=255, default='')
    phone= models.IntegerField(default='')
    email = models.EmailField(default='')
    date = models.DateTimeField(default='')
    
    def __str__(self):
        return self.name