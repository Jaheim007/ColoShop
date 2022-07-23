from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import NewsLetter, Contact, Banner, Service, Site_Info
from Shop.models import Category, Product, ProductColour, ProductImage, Promotion, Comments, DealOfTheWeek, Best_Sellers 



class Home(View):
    template_name = 'pages/index.html'
    
    def get(self,request): 
        categories = Category.objects.filter(active=True)
        products = Product.objects.filter(active=True)
        return render(request, self.template_name, locals())
    
    def post(request):
        pass
    
def updatecart(request):
    return JsonResponse("Cart Updated", safe=False )

class Shop(View):
    template_name = 'pages/categories.html'
    
    def get(self, request):
        return render(request, self.template_name, locals())
    
    def post(request):
        pass
    
def contact(request):
    return render(request, "pages/contact.html")
    
def verification(request):
    msg =''
    success = True
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        website = request.POST.get("website")
        message = request.POST.get("message")
        
        contact = Contact(
            name = name, 
            email = email, 
            website = website, 
            message = message
        )
        
        contact.save()
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
