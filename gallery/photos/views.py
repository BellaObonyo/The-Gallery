from django.db.models import query
from django.http import request
from django.shortcuts import redirect, render
from photos.models import Image
# Create your views here.
def index(request):
    images=Image.objects.all()
    return render(request,'index.html',{"images":images})

    
def search_photos_category(request):
    
    della=Image.objects.all()
    if "pen" in request.GET:
         query=request.GET["pen"]
         della=Image.objects.filter(location__name__icontains=query)
    
    return render(request,'search.html',{"della":della})
    
    