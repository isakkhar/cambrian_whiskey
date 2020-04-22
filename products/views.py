# import Http Response from django
from django.shortcuts import render

# not sure if i need to import Product_description from .models file
from .models import Product

# Create your views here.

def all_products_view(request):
  """return all the products in the database
  """
  products = Product.objects.all()
  """render a products html page and within that page we will have access to products, so all_products"""
  return render(request, 'products.html', {'products': products})