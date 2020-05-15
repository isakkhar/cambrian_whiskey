from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product


# Create your views here.

def index(request):
  """ A view that displays the index page """
  return render(request, 'index.html')

def about(request):
  """
  Sends the user to the about page
  """
  # product = Product.objects.all()
  # context = {'product': product}
  return render(request, 'about.html')