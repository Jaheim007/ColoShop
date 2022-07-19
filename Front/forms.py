
from os import lseek
from django import forms
from django.forms import ModelForm
from Clients.models import Connection, Register

class ConnectForm(ModelForm):
    class Meta:
        model = Connection
        fields = [ 
            "email", 
            "password" 
        ]

        widgets = {
            'email': forms.EmailInput(),
            'password': forms.PasswordInput()
        }
        
class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = [
            "first_name", 
            "last_name", 
            "email", 
            "password", 
            "confirm_password"
        ]
        
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput()
        }
