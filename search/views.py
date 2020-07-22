from django.shortcuts import render
from products.models import Product
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def whiskey_search(request):
  products = Product.objects.filter(title__icontains=request.GET['q']).order_by('title')

  paginator = Paginator(products, 6)
  page_number = request.GET.get('page', 1)
  page = paginator.page(page_number)

  # print(request.META.get('PATH_INFO', None))
  return render(request, 'products.html', {'page':page})



# THIS IS THE MESSAGE FROM HALEY : "Currently you're getting the string to search by using the line request.GET['q'] . If you print this (request.GET['q'] , which you're expecting to be equal to the query string that you're typing in in your search bar) to your terminal and try to search something, does it print what you typed in in your search bar in the terminal? " This is a good way for future reference to see if the search bar functionality works

