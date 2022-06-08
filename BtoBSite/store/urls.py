from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home-page"), #slash in front is unnessessary
    path('parts/search', views.searchedValue, name="searchedPage"), #struggling because I wanted to have the same url more or less for two URLS
    #Has to go first as parts/search would always go to the other view otherwise
    path('parts/<str:category_chosen>', views.filteredParts, name="filteredPage"), #order really matters here
    #^ this works because our JS is passing a category_chosen parameter to this path
    # If we just had an html url reference to this path, it would create an erorr noreverse match
    path('parts', views.parts, name="partsPage"),
]