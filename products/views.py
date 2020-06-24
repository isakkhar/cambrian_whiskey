# import Http Response from django
from django.shortcuts import render
from django.core.paginator import Paginator

# not sure if i need to import Product_description from .models file
from .models import Product

# Create your views here.

def all_products_view(request):
  """return all the products in the database
  """
  products = Product.objects.all()
  paginator = Paginator(products, 6)
  page_number = request.GET.get('page', 1)
  page = paginator.page(page_number)
  """render a products html page and within that page we will have access to products, so all_products"""

  if page.has_next():

    next_url = f'?page={page.next_page_number()}'

  else:

    next_url = ''

  if page.has_previous():

    prev_url = f'?page={page.previous_page_number()}'

  else:

    prev_url = ''

  
  return render(request, 'products.html', {'page': page, 'next_page_url': next_url, 'prev_page_url': prev_url})





