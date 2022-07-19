from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField



class Connection(models.Model):
    class Meta:   
        verbose_name_plural = 'Connection' 
        
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
        
    def __str__(self):
        return self.username
        
class Register(models.Model):
    class Meta:   
        verbose_name_plural = 'Register' 
        
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
        
    def __str__(self):
        return self.first_name

    
    
    
     
       
    

