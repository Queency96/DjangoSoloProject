from django.contrib import admin
from . import models

# Register your models here.
#admin.site.register(models.MarketProduct)

@admin.register(models.MarketProduct)
class ProductsAdmin(admin.ModelAdmin):
  list_display = ['product_name', 'description', 'price']
  