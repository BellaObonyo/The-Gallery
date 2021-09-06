from django.http import request
from django.shortcuts import redirect, render
from photos.models import Image
# Create your views here.
def index(request):
    images=Image.objects.all()
    return render(request,'index.html',{"images":images})
