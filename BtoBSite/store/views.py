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
    categories = Category.objects.all()
    return render(request, 'partsPage.html',{
        'parts':parts,
        'categories':categories
    })

def filteredParts(request, category_chosen):
    print(category_chosen)
    parts = Part.objects.filter(category__name = category_chosen) #to get foreign
    #key attributes, you have to use underscores to get the field name of related fields accross models
    #
    print(parts)
    categories = Category.objects.all()
    return render(request, 'partsPage.html',{
        'parts':parts,
        'categories':categories
    })