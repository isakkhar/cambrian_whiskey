from django.shortcuts import render
from products.models import Product

# Create your views here.

def whiskey_search(request):
  products = Product.objects.filter(title__icontains=request.GET['q'])
  print(request.META.get('PATH_INFO', None))
  return render(request, 'products.html', {'products':products})

