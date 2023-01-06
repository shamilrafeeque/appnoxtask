from django.contrib import admin
from .models import Products
# Register your models here.
class adminProduct(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'price','images','stock','is_available') 


admin.site.register(Products,adminProduct)