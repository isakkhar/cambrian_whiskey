from django.test import TestCase
from .models import Product
# Create your tests here.

# each time i create a model in the models.py file i will test here

class TestProductModel(TestCase):
  """
  Here we'll define the tests
  that we'll run against our Product models
  """

  def test_product_title(self):
    test_title = Product(title = 'A Product')
    self.assertEqual(str(test_title), 'A Product')

  def test_productdescription(self):
    test_description = Product(description = 'A whiskey made in the Highlands')
    self.assertEqual(str(test_description), 'A whiskey made in the Highlands')




