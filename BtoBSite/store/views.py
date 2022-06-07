from msilib.schema import Error
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Part, Category, Brand
from django.core.paginator import Paginator
# Create your views here.
def homePage(request):
    return render(request, 'home.html',{
        
    })
def parts(request):
    parts=Part.objects.all() #get all part objects in the DB
    categories = Category.objects.all()
    brands = Brand.objects.all()
    
    paginator = Paginator(parts, 1)
    page = request.GET.get('page')
    parts = paginator.get_page(page)

    return render(request, 'partsPage.html',{
        'parts':parts,
        'categories':categories,
        'brands': brands,
        
    })

def filteredParts(request, category_chosen):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    
    for category in categories:
        if category_chosen == str(category): #If true we are filtering by category, not brand
            partsByType = Part.objects.filter(category__name = category_chosen) #to get foreign
            #key attributes, you have to use underscores to get the field name of related fields accross models
            return render(request, 'partsPage.html',{
                'parts':partsByType,
                'categories':categories,
                'brands':brands,
            })
    #if did not filter by category, then we had to have by brand, this could go poorly if add
    #more filtering options
    partsByBrand = Part.objects.filter(brand__brand = category_chosen) 
    return render(request, 'partsPage.html',{
                'parts':partsByBrand,
                'categories':categories,
                'brands':brands,
            })
   

    
        

    #request currently does not know what to do if use same function to go thru multiple
    # queries, as some values might not be found 



    
  
 