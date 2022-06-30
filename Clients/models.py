from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

class Clients(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    birth_date = models.DateField(null=True, blank=True)
    image = models.URLField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Clients.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.clients.save()

    class Meta:
        verbose_name_plural = 'Clients'
        
    def __str__(self):
        return self.user.first_name
    

    
    
    
     
       
    

