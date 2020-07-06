# unlike the products app where we created a models.py file and putting products in our database, in this case the cart items will not go into the database they will just be stored in the session when the user is logged in. So that user can add products to the cart but when they log out that cart will be lost

from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
  """
  Ensures that the cart contents are available when rendering every page
  """
  """ here we have a cart thats requesting the session so request the existing cart if there is one and a blank dictionary if there isnt one
  """

  cart = request.session.get('cart', {})

  # initialise the following:

  cart_items = []
  total = 0
  product_count = 0
  for id, quantity in cart.items():
    product = get_object_or_404(Product, pk=id)
    total += quantity * product.price
    product_count += quantity
    cart_items.append({'id':id, 'quantity':quantity, 'product':product})

  return { 'cart_items': cart_items, 'total':total, 'product_count':product_count }






