from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.
# we need to add those models we just created in the checkout/models.py file otherwise we would be unable to edit them through the admin panel

class OrderLineAdminInline(admin.TabularInline):
  model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
  inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)
