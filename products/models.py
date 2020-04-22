from django.db import models

# Create your models here.
# this is what will create the database for our product. This is where we specify our columns in our database

class Product(models.Model):
  REGION = 'region'
  EUROPE = 'europe'
  AMERICA = 'america'
  REST_OF_WORLD = 'rest_of_world'
  PRODUCT_REGION_CHOICES = (
    (EUROPE, 'Europe'),
    (AMERICA, 'America'),
    (REST_OF_WORLD, 'Rest_Of_World')
  )

  title = models.CharField(max_length=254, default='')
  description = models.TextField(max_length=800, blank=False)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image = models.ImageField(upload_to='images', null=True)
  region = models.CharField(max_length=13, choices=PRODUCT_REGION_CHOICES, default=EUROPE)

  def __str__(self):
    return self.title

class Product_description(models.Model):
  title = models.CharField(max_length=254, default='')
  description = models.TextField(max_length=800, blank=False)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image = models.ImageField(upload_to='images', null=True)
  

  def __str__(self):
    return self.description





