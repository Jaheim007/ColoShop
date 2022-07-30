from django.shortcuts import render, redirect, get_object_or_404
from Shop.models import Product
from Cart import models
from django.core.exceptions import ObjectDoesNotExist

#Creating the Cart
def session_cart_id(request):
    cart = request.session.session_key #The Cart
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    try:
        cart = models.Cart.objects.get(session_id = session_cart_id(request)) # get the cart using the session_id in the session
    except models.Cart.DoesNotExist:
        cart = models.Cart.objects.create(
            session_id = session_cart_id(request)
        )
    cart.save()
    
    try:
        cart_item = models.CartItems.objects.get(product = product , cart = cart)
        cart_item.quantity += 1  #EveryTime a product is added its quatity will rise.
        cart_item.save()
        
    except models.CartItems.DoesNotExist:
        cart_item = models.CartItems.objects.create(
            product = product, 
            quantity = 1, 
            cart = cart,
        )
        cart_item.save()
    return redirect("cart")
    
def remove_item(request, product_id):
    cart = models.Cart.objects.get(session_id = session_cart_id(request))
    product = get_object_or_404(Product, id = product_id) #if the object is present it will return the object or else it will return error 404 
    cart_item = models.CartItems.objects.get(product = product , cart = cart)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        
    else:
        cart_item.delete()
    return redirect("cart")


def Cart(request, total = 0 , quantity = 0 , cart_items = None):
    try:
        cart = models.Cart.objects.get(session_id = session_cart_id(request)) #To get the same Session 
        cart_items = models.CartItems.objects.filter(cart = cart , is_active = True) #I filtered to get the same cart and active = true
        for cart_item in cart_items:
            total += (cart_item.product.original_price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass
         
    return render(request, "pages/cart.html", locals())







