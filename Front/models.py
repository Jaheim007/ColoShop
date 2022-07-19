from django.db import models
from Shop.models import Promotion
from phonenumber_field.modelfields import PhoneNumberField

class NewsLetter(models.Model):   
    class Meta:
        verbose_name = 'NewsLetter'
        verbose_name_plural = 'NewsLetters'  
 
    email = models.EmailField(max_length=50, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email
    
class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts' 
        
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
       
class Banner(models.Model):   
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners' 
          
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    product_on_promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, related_name="banner_product")
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Service(models.Model):
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'   
             
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self) -> str:
        return self.title
    
class Site_Info(models.Model): 
    class Meta:
        verbose_name = 'Site_Info'
        verbose_name_plural = 'Site_Infos'   
        
    site_name = models.CharField(max_length=100)
    section_new_arrivals_title = models.CharField(max_length=50)
    section_deals_title = models.CharField(max_length=30)
    facebook_link = models.URLField()
    twitter_link = models.URLField() 
    instagram_link = models.URLField()
    skype_link = models.URLField()
    pinterest_link = models.URLField()
    copyright = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    opening_days = models.CharField(max_length=255)
    closed_day = models.CharField(max_length=254)
    phone = PhoneNumberField()
    map_location = models.URLField()
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.site_name

    