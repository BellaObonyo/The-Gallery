from django.http import request
from django.shortcuts import redirect, render
from photos.models import Image
# Create your views here.
def index(request):
    images=Image.objects.all()
    return render(request,'index.html',{"images":images})

    
def search_photos_category(request):
  if 'photo' in request.GET and request.GET["photo"]:
    search_term = request.GET.get("photo")
    searched_photos = Image.search_photos_by_category(search_term)
    message = f"{search_term}"

    return render(request, 'search.html', {"message":message,"photos":searched_photos})

  else:
    message = 'You have not searched for any term'
    return render(request, 'search.html', {"message":message})    
