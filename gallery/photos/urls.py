from os import name
from django.conf.urls import include
from django.urls import path
from .views import index,search_photos_category
urlpatterns = [
    path('',index,name="home"),
    path('search/',search_photos_category, name="new")
]