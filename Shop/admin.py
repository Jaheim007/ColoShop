from django.contrib import admin
from .models import  Order, OrderItem, Product, Category, ProductColour, ProductImage, Promotion, Comments, DealOfTheWeek, Best_Sellers, Customer

@admin.register(Customer)
class Customers(admin.ModelAdmin):
    
    list_display = (
        'user',
        'name',
        'email'
    )

@admin.register(Product)
class Product(admin.ModelAdmin):

    list_display = (
        'name',
        'original_price',
        'promotion_reduction',
        'promotion_percentage',
        'stock', 
        'size',
        'image',
        'active',
        'is_promotion',
        'is_solde'
    )

@admin.register(Category)
class Category(admin.ModelAdmin):

    list_display = (
        'name',
        'description',
        'active',
        'image'
    )
    
@admin.register(Promotion)
class Promotion(admin.ModelAdmin):
    
    list_display = (
        'product',
        'active'
    )
    
@admin.register(ProductColour)
class ProductColour(admin.ModelAdmin):
    
    list_display = (
        'product',
        'colour',
        'colour_code'
    )
    
@admin.register(ProductImage)
class ProductImage(admin.ModelAdmin):
    
    list_display = (
        'product',
        'images'
    )
    
@admin.register(Comments)
class Comments(admin.ModelAdmin):
    
    list_display = (
        'clients',
        'product',
        'message'
    )
    
@admin.register(Best_Sellers)
class Best_Sellers(admin.ModelAdmin):
    
    list_display = (
        'product',
        'active'
    )
    
@admin.register(DealOfTheWeek)
class DealOfTheWeek(admin.ModelAdmin):
    
    list_display = (
        'deal_time',
        'products'
    )
    
@admin.register(Order)
class Order(admin.ModelAdmin):
    
    list_display = (
        'customer',
        'date_ordered',
        'complete',
        'transaction_id'
    )
    
@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    
    list_display = (
        'product',
        'quantity',
        'date_added'
    )

