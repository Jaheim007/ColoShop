from django.contrib import admin
from .models import Cart, CartItems 

@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display =(
        "session_id",
        "date_added"
    )
    
@admin.register(CartItems)
class CartItems(admin.ModelAdmin):
    list_display =(
        "product",
        "cart",
        "quantity",
        "is_active"
    )

# Register your models here.
