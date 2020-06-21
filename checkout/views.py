# get_object_or_404 is when u get the product id from the product being purchased

from django.shortcuts import render, get_object_or_404, reverse, redirect

from django.contrib.auth.decorators import login_required
# stripe will control the security of the money transaction but we must inform the customer if they have made an error
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.
# we have created models and forms but no way of rendering that in our html so we need to add some views

# SO OUR VIEW IS TO REQUIRE THE API KEYS 
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
  if request.method=='POST':
    order_form = OrderForm(request.POST)
    payment_form = MakePaymentForm(request.POST)

    # an if statement here that says if order form and payment form is filled out correctly then the orderform will be saved 

    if order_form.is_valid() and payment_form.is_valid():
      order = order_form.save(commit=False)
      order.date = timezone.now()
      order.save()

      # now we need to get the info on what has been purchased
      cart = request.session.get('cart', {})
      # we initailaise a total of zero then do a for loop
      total = 0
      for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        order_line_item = OrderLineItem(
          order = order,
          product = product,
          quantity = quantity
        )
        order_line_item.save()
        # now that we know what they want to buy were putting a try exception here and it will create a customer, charge, so thats using stripes inbuilt api here
      try:
        customer = stripe.Charge.create(
          amount = int(total * 100),
          currency = 'UK',
          # description: if we go to our stripe dashboard we would be able to see who the payment came from
          description = request.user.email,
          card = payment_form.cleaned_data['stripe_id'],
        )
      except stripe.error.CardError:
        messages.error(request, 'Your card was declined')

      if customer.paid:
        messages.error(request, 'You have successfuly paid')
        # we request the cart from the current session
        request.session['cart'] = {}
        # we need reverse and redirect import at the top of the page. Below we return reverse products, so that just takes them back to the products html page
        return redirect(reverse('products'))
      else:
        messages.error(request, 'Unable to take payment')
    else:
      print(payment_form.errors)
      messages.error(request, 'We were unable to take a payment with that card!')
  else:
    payment_form = MakePaymentForm()
    order_form = OrderForm()
  return render(request, 'checkout.html', {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})

# for the checkout.html to work we must create urls.py in checkout directory



    




