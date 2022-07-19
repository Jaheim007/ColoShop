from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .forms import ConnectForm, RegisterForm
from .models import NewsLetter, Contact, Banner, Service, Site_Info
from Shop.models import Category, Product, ProductColour, ProductImage, Promotion, Comments, DealOfTheWeek, Best_Sellers 
from Clients.models import Register


class Home(View):
    template_name = 'pages/index.html'
    
    def get(self,request): 
        categories = Category.objects.filter(active=True)
        products = Product.objects.filter(active=True)
        return render(request, self.template_name, locals())
    
    def post(request):
        pass

class Shop(View):
    template_name = 'pages/categories.html'
    
    def get(self, request):
        return render(request, self.template_name, locals())
    
    def post(request):
        pass

class Contact(View):
    template_name = 'pages/contact.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(request):
        pass
    
class Connection(View):
    template_name = 'pages/connect.html'
    
    def get(self, request):
        connectForm = ConnectForm()
        return render(request, self.template_name, locals())
    
    def post(request):
        pass
    
class Registeration(View):
    template_name = 'pages/register.html'
    
    def get(self , request):
        registerForm = RegisterForm()
        return render(request, self.template_name, locals())
    
    def post(request):
        msg =''
        success = True
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
        
        register = Register(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password,
            confirm_password = confirm_password
        )
        
        register.save()
        msg = 'Un message a été envoyé à votre adresse e-mail'
        
        data = {
        'msg': msg,
        'success': success
        }
        return JsonResponse(data, safe=False)
    
class ShopSingle(View):
    template_name = 'pages/single.html'
    
    def get(self , request):
        return render(request, self.template_name)
    
    def post(self, request):
        pass
    
class Cart(View):
    template_name = 'pages/cart.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(request):
        pass
        


# Create your views here.
