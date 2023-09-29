from django.test import TestCase
from apps.tours import models




class TestCategoryModel(TestCase):
    def setUp(self):
        self.category_name = 'Restaurants'
        self.category = models.Category(cat = self.category_name)
        
    def test_create_category_object_successful(self):
        self.assertIsInstance(self.category, models.Category)
        
    def test_category_method__str(self):
        self.assertEqual(str(self.category), self.category_name)
        
    def test_category_meta_verbose_name_plural(self):
        name = "Categories"
        #self.assertEqual(name, models.Category._meta.verbose_name_plural)
        self.assertEqual(name, self.category._meta.verbose_name_plural)