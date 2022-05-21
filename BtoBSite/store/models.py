
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 200, unique=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    brand = models.CharField(max_length= 50, unique=True)

    def __str__(self):
        return self.brand

class Part(models.Model):
    title = models.CharField(max_length = 200)
    partID = models.CharField(max_length = 200, unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    isAvailable = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'images')
    
    def __str__(self):
        return self.title