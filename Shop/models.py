from random import choices
from django.db import models
from multiselectfield import MultiSelectField

class Category(models.Model):    
    Category_name = models.CharField(max_length=50)
    Category_Image = models.URLField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

class Products(models.Model): 
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    XL = 'XL'
    XXL = 'XXL'
    
    SIZE = [
        (SMALL, 'small'),
        (MEDIUM, 'medium'),
        (LARGE, 'large'),
        (XL, 'xl'),
        (XXL, 'xxl'),
    ]
    
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    YELLOW = "YELLOW"
    BLACK = "BLACK"
    
    COLOUR = [
        (RED, "red"), 
        (BLUE, "blue"), 
        (ORANGE, "orange"), 
        (YELLOW, "yellow"),
        (BLACK, "black")
    ]

    
    Product_name = models.CharField(max_length=20, blank=False)
    Product_price = models.FloatField(max_length=50, blank=False)
    Product_Currency = models.CharField(max_length=6)
    Product_Colour = MultiSelectField(choices= COLOUR)
    Product_Colour_Tag = models.CharField(max_length=20)
    Product_Reduction = models.CharField(max_length=4)
    Product_Fixed = models.FloatField(max_length=50)
    Size = MultiSelectField(choices=SIZE)
    Image = models.URLField()
    New = models.BooleanField(default=True)
    Sale = models.BooleanField(default=False)
    Prom_Time = models.DurationField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products_category")
    
    created_at = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)   
    

