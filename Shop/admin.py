from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class Product(admin.ModelAdmin):

    list_display = (
        'categories',
        'Product_name',
        'Product_price',
        'Product_Currency',
        'Product_Colour',
        'Product_Reduction', 
        'Product_Fixed',
        'Size',
        'New',
        'Sale',
        'Prom_Time'
    )

@admin.register(Category)
class Category(admin.ModelAdmin):

    list_display = (
        'Category_name',
        'Category_Image'
    )

# Register your models here.
