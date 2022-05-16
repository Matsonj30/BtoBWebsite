from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home-page"), #slash in front is unnessessary
    path('parts/<str:category_chosen>', views.filteredParts, name="filteredPage"), #order really matters here
    path('parts', views.parts, name="partsPage"),
   
]