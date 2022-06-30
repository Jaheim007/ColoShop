from django.contrib import admin
from .models import Clients

@admin.register(Clients)
class Client_admin(admin.ModelAdmin):
    
    list_display = (
        'user', 
        'phone_number', 
        'birth_date', 
        'updated_at'
    )




# Register your models here.
