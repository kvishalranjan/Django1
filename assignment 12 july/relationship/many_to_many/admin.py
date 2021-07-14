from django.contrib import admin
from .models import *

# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier_name', 'supplier_address')
    list_filter = ('supplier_name',) 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_desc',)
    list_filter = ('product_name',)

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)

