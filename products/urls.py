# so we are going to create a urls.py within the products app which will be linked in the top level urls in the cammbrian_whiskey

# Create a url path to map to the functions listed in the views.py file 

from django.conf.urls import url, include
from .views import all_products_view

urlpatterns = [
  url(r'^$', all_products_view, name='products'),
]