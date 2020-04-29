# now that we have a database to store our customer info we need someway for the customer to input it hence a forms.py

from django import forms
from .models import Order

class MakePaymentForm(forms.Form):

  MONTH_CHOICES = [(i, i) for i in range(1, 13)]
  YEAR_CHOICES = [(i, i) for i in range(2020, 2040)]

  credit_card_number = forms.CharField(label='Credit card number', required=False)
  cvv = forms.CharField(label='Security code (CW)', required=False)
  expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
  expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
  # stripe requires an id and even though we have included it into the form, the user will not see this
  # HiddenInput is something that will be inputted into the form but hidden from the user
  stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ('full_name', 'street_address1', 'street_address2', 'town_or_city', 'county',  'country', 'postcode', 'phone_number')






