from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Part, Category
# Create your views here.
def homePage(request):
    return render(request, 'home.html',{
        
    })
def parts(request):
    parts=Part.objects.all() #get all part objects in the DB
    return render(request, 'partsPage.html',{
        'parts':parts
    })