from msilib.schema import Error
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Part, Category, Brand
# Create your views here.
def homePage(request):
    return render(request, 'home.html',{
        
    })
def parts(request):
    parts=Part.objects.all() #get all part objects in the DB
    categories = Category.objects.all()
    brands = Brand.objects.all()

    return render(request, 'partsPage.html',{
        'parts':parts,
        'categories':categories,
        'brands': brands,
    })

def filteredParts(request, category_chosen):
    print(category_chosen)
   
    partsByType = Part.objects.filter(category__name = category_chosen) #to get foreign

    #key attributes, you have to use underscores to get the field name of related fields accross models
        
    """  partsByBrand = Brand.objects.filter(brand__name = category_chosen) """
    #request currently does not know what to do if use same function to go thru multiple
    # queries, as some values might not be found 



    categories = Category.objects.all()
    brands = Brand.objects.all()
  
    return render(request, 'partsPage.html',{
        'parts':partsByType,
        'categories':categories,
        'brands':brands,
    })
   