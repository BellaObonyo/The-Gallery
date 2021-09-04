from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Editor, Location,Image

admin.site.register(Editor)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)

