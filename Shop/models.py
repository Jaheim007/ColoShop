from django.db import models
from multiselectfield import MultiSelectField

class Category(models.Model):    
    Category_name = models.CharField(max_length=50)
    Category_Image = models.URLField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.Category_name

class Product(models.Model): 
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    XL = 'XL'
    XXL = 'XXL'
    
    SIZE = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (XL, 'XL'),
        (XXL, 'XXL'),
    ]
    
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    YELLOW = "YELLOW"
    BLACK = "BLACK"
    
    COLOUR = [
        (RED, "Red"), 
        (BLUE, "Blue"), 
        (ORANGE, "Orange"), 
        (YELLOW, "Yellow"),
        (BLACK, "Black")
    ]

    RED_TAG = '#FF0000'
    BLUE_TAG = '#0000FF'
    ORANGE_TAG = '#FFA500'
    YELLOW_TAG = '#FFFF00'
    BLACK_TAG = '#000000'

    COLOUR_TAGS = [ 
        (RED_TAG, '#FF0000'),
        (BLUE_TAG, '#0000FF'),
        (ORANGE_TAG,'#FFA500'),
        (YELLOW_TAG, '#FFFF00'),
        (BLACK_TAG,'#000000')
    ]

    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products_category")
    Product_name = models.CharField(max_length=20, blank=False)
    Product_price = models.FloatField(max_length=50, blank=False)
    Product_Currency = models.CharField(max_length=6)
    Product_Colour = MultiSelectField(choices= COLOUR)
    Product_Colour_Tag = MultiSelectField(choices= COLOUR_TAGS)
    Product_Reduction = models.CharField(max_length=4, blank=True)
    Product_Fixed = models.FloatField(max_length=50, blank=True)
    Size = MultiSelectField(choices=SIZE)
    Image = models.URLField()
    New = models.BooleanField(default=False)
    Sale = models.BooleanField(default=False)
    Prom_Time = models.DurationField(blank=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)   
    

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self) -> str:
        return self.categories.Category_name