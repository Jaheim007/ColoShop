from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from Clients import forms

class Register(View):      
    template_name  = "pages/register.html"
    
    def get(self, request):   
        form = forms.NewUserForm   
        return render(request, self.template_name, locals()) 
    
    def post(self, request):  
        if request.method == "POST": 
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            user = User(
                first_name = first_name,
                last_name = last_name,
                username = username, 
                email = email, 
                password = password1,  
            )
            
            user.save()
            login(request, user)
            return redirect("/connect")
        
        return render(request, self.template_name,locals()) 

class Connection(View): 
    form = forms.LoginForm  
    template_name  = "pages/connect.html"
    
    def get(self , request):
        
        return render(request, self.template_name, context={"form": self.form}) 
    
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():     
            user = authenticate(
                username=form.cleaned_data["username"], 
                password= form.cleaned_data["password"]
            )
            print(user)
            if user is not None:
                login(request, user)
                return redirect("/") 
            else:     
                print("User not Found") 
                
        return render(request, self.template_name,locals()) 
    