
from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 200, unique=True)

    def __str__(self):
        return self.name

class Part(models.Model):
    title = models.CharField(max_length = 200)
    partID = models.CharField(max_length = 200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    isAvailable = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'images')

    def __str__(self):
        return self.title