from itertools import product
from django.db import models
from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator
from Clients.models import *
import datetime

class Customer(models.Model): 
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return str(self.user)

class Category(models.Model):  
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    #Models Creation for Category 
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "Category_Images")
    description = models.TextField()
    active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self) -> str:
        return self.name

class Product(models.Model): 
    class Meta:
        verbose_name_plural = 'Products'
        
    #Models for the Products Sections
    name = models.CharField(max_length=20, blank=False)
    original_price = models.FloatField(max_length=50, blank=False)
    promotion_reduction = models.PositiveIntegerField(default=0)
    promotion_percentage = models.PositiveIntegerField(validators=[MaxValueValidator(100)],default=0)
    stock = models.PositiveIntegerField()
    
    size = models.CharField(max_length=10)
    image = models.ImageField(upload_to = "Products_Images")
   
    categories = models.ManyToManyField(Category, related_name="product_category")
    
    active = models.BooleanField(default=True)
    is_promotion = models.BooleanField(default=False)
    is_solde = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)   
    
    #This Function is for when an article is new 
    def is_new(self):
        
        now = 
        datetime.datetime.now()
        
        dif_date = now - self.created_at 
        
        return dif_date.days < 2
    
    #This function is for when an article has a reducation price 
    def get_product_reduction(self):
        
        if self.promotion_percentage :
            
            return self.original_price * self.promotion_percentage // 100
        
        return self.promotion_reduction
        
    
    #This function is for when an is on promotion
    def get_final_product_price(self):
        
        if self.is_promotion:
            
            if self.promotion_percentage :
                
                reduction = self.original_price * self.promotion_percentage // 100
                
                return self.original_price - reduction
            
            elif self.promotion_reduction:
                
                return self.original_price - self.promotion_reduction
            
            else:
                
                return self.original_price
        else:
            
            return self.original_price
        
        
    def __str__(self) -> str:
        return self.name
    
class ProductColour(models.Model):
    
    product = models.ForeignKey(Product, related_name="product_colour", on_delete=models.CASCADE)
    colour = models.CharField(max_length=100)
    colour_code = ColorField(default='#FF0000')
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)   
    
    def __str__(self) -> str:
        return self.colour
    
class Comments(models.Model):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    clients = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="clients_comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_comments")
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self) -> str:
        return self.clients.uesr.first_name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    images = models.ImageField(upload_to = "Additional Product Images")
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)  
    
    def __str__(self) -> str:
        return self.product.name
    
class Promotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="promotion_product")
    active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.product.name
    

class DealOfTheWeek(models.Model):
    deal_time = models.DateTimeField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="deal_product")
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.products.name

class Best_Sellers(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sellers_product")
    active = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.product.name

