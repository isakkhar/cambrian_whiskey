# now that we have a database to store our customer info we need someway for the customer to input it hence a forms.py

from django import forms
from .models import Order

class MakePaymentForm(forms.Form):

  MONTH_CHOICES = [(i, i) for i in range(1, 13)]
  YEAR_CHOICES = [(i, i) for i in range(2020, 2040)]

  credit_card_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Credit Card Number'}), required=False)
  cvv = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Cvv'}), required=False)
  # expiry_month = forms.ChoiceField(label='', choices=MONTH_CHOICES, required=False)
  # expiry_year = forms.ChoiceField(label='', choices=YEAR_CHOICES, required=False)
  expiry_month = forms.ChoiceField(label='', choices=MONTH_CHOICES, widget=forms.TextInput(attrs={'placeholder': 'Month'}), required=False)
  expiry_year = forms.ChoiceField(label='', choices=YEAR_CHOICES, widget=forms.TextInput(attrs={'placeholder': 'Year'}), required=False)
  # stripe requires an id and even though we have included it into the form, the user will not see this
  # HiddenInput is something that will be inputted into the form but hidden from the user
  stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
  full_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
  street_address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Address 1'}))
  street_address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Address 2'}))
  town_or_city = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Town/City'}))
  county = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'County'}))
  country = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Country'}))
  postcode = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Postcode'}))
  phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

  class Meta:

    model = Order
    
    fields = ('full_name', 'street_address1', 'street_address2', 'town_or_city', 'county',  'country', 'postcode', 'phone_number')

    widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'street_address1': forms.TextInput(attrs={'placeholder': 'Address line 1'}), 'street_address2': forms.TextInput(attrs={'placeholder': 'Address line 2'}), 'town_or_city': forms.TextInput(attrs={'placeholder': 'Town/City'}), 
            'county': forms.TextInput(attrs={'placeholder': 'County'}), 
            'country': forms.TextInput(attrs={'placeholder': 'Country'}), 
            'postcode': forms.TextInput(attrs={'placeholder': 'Address line 1'}), 
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'})
        }


