from os import name
from gallery.photos.models import Category, Image, Location
from django.test import TestCase

# Create your tests here.
class testImage(TestCase):
    def setUp(self):
        self.location=Location(name='Grill')
        self.location.save_location()

        self.category=Category(name='Jill')
        self.category.save_category()

        self.image=Image(id=1,description='longblue',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        saved=Image.objects.all()
        self.assertTrue(len(saved) > 0)   

    def test_delete_image(self):
        self.image.delete_image()
        deleted=Image.objects.all()
        self.assertTrue(len(deleted) == 0) 

    def test_search_by_category(self):
        image_category=''
        result=self.image.search_by_category(image_category)
        self.assertTrue(len(result) >=0)

class TestCategory(TestCase):
    def setUp(self):
        self.image_category=Category(name='violet')
        self.image_category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_category, Category))

    def test_save_category(self):
        self.image_category.save_category()
        category=Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_category(self):
        self.image_category.delete_category()
        category=Category.objects.all()
        self.assertTrue(len(category) ==0)

class TestLocation(TestCase):
    def setUp(self):
        self.image_location=Location(name='nature')
        self.image_location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_location, Location))

    def test_save_location(self):
        self.image_location.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_location(self):
        self.image_location.delete_location()
        location=Location.objects.all()
        self.assertTrue(len(location) ==0)


