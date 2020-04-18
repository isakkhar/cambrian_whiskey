from django.db import models

# Create your models here.
# this is what will create the database for out product. This is where we specify our columns in our database

class Product(models.Model):
  title = models.CharField(max_length=254, default='')
  description = models.TextField(max_length=800, blank=False)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image = models.ImageField(upload_to='images', null=True)
  

  def __str__(self):
    return self.title



