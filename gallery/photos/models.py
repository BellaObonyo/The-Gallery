from cloudinary.uploader import upload
from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE


# Create your models here.
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

        
    class Meta:
        verbose_name_plural='CATEGORIES'

    def __str__(self):
        return self.name
class Location(models.Model):
    name = models.CharField(max_length =30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    class Meta:
        verbose_name_plural='LOCATIONS'

    def __str__(self):
        return self.name

class Image(models.Model):
    description= models.CharField(max_length =60)
    location = models.ForeignKey(Location,on_delete=CASCADE)
    category = models.ForeignKey(Category,on_delete=CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery/',default='no photo')  

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_name(cls):
        Bella=cls.objects.all()
        return Bella

    def __str__(self):
        return self.description

    @classmethod
    def search_by_category(cls,category):
        images=cls.objects.filter(image_category__name__icontains=category)
        return images
    
    @classmethod
    def get_image_by_id(cls, id):
        image_id=cls.objects.filter(id=id).all()
        return image_id


