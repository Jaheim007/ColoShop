from audioop import maxpp
from django.db import models

class NewsLetters(models.Model):      
    email = models.EmailField(max_length=50, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Banner(models.Model):     
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    Image = models.URLField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

class Info(models.Model):       
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)    
    
class Site_Info(models.Model):   
    Site_name = models.CharField(max_length=100)
    Section_New_Arrivals = models.CharField(max_length=50)
    Section_Deal = models.CharField(max_length=30)
    Facebook_link = models.URLField()
    Twitter_link = models.URLField() 
    Instagram_link = models.URLField()
    Skype_link = models.URLField()
    Pinterest = models.URLField()
    Copyright = models.
     
    
    
