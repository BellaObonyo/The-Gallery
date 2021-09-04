from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
# Create your models here.
class Image(models.Model):
    description= models.CharField(max_length =60)
    editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
    location = models.ManyToManyField('Location')
    category = models.ManyToManyField('Category')
    pub_date = models.DateTimeField(auto_now_add=True)
    name_image = models.ImageField(upload_to = 'articles/', default='default.jpg')
    image = CloudinaryField('image')  

    @classmethod
    def get_name(cls):
        Bella=cls.objects.all()
        return Bella
    def __str__(self):
        return self.description
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    

    def save_editor(self):
        self.save()

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length =30)

    class Meta:
        verbose_name_plural='CATEGORIES'

    def __str__(self):
        return self.name
class Location(models.Model):
    name = models.CharField(max_length =30)

    class Meta:
        verbose_name_plural='LOCATIONS'

    def __str__(self):
        return self.name

