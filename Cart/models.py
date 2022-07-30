from django.db import models
from Shop.models import Product


class Cart(models.Model):
    session_id = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.session_id)
    
class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.original_price * self.quantity
    
    def __str__(self):
        return str(self.product)
# Create your models here.
