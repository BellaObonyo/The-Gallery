from django.http import request
from django.shortcuts import redirect, render
from photos.models import Image
# Create your views here.
def index(request):
    Jane=Image.get_name()
    return render(request,'index.html',{"Jane":Jane})
