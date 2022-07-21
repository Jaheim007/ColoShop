from django.conf import settings
from .models import Product
class Cart(object):
    
    def __init__(self , request):
        """Initializing of the Cart"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, product, quantity =1, override_quantity=False):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : 0, 'price' : str(product.original_price)}
        
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        
    def remove(self, product):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.object.filter(id__in=product_ids)
      
            
        