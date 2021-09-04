from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Editor,pub_date, Location, name_image

admin.site.register(Editor)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(pub_date)
admin.site.register(name_image)
