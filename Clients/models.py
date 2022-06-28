from posixpath import isabs
from pyexpat import model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model): 
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, blank=False)
    phone_number = PhoneNumberField(region="CIV")
    birth_date = models.DateField(blank=False)
    image = models.URLField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
    
    
     
       
    

