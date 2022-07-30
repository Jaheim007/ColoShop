from os import name
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
        sellers = Best_Sellers.objects.filter(active = True)
        return render(request, self.template_name, locals())
    
    def post(request):      
        msg =''
        success = True
        if request.method == "POST":
            email = request.POST.get("email")
        
        newsletters = NewsLetter( 
            email = email, 
        )
        
        newsletters.save()
        msg = 'Votre message a éte reçu'
            
        data = {
            'msg': msg,
            'success': success
            }
        
        return JsonResponse(data, safe=False)
            
    
def updatecart(request):
    return JsonResponse("Cart Updated", safe=False)

class Shop(View):
    template_name = 'pages/categories.html'
    
    def get(self, request):
        categories = Category.objects.filter(active=True)
        products = Product.objects.filter(active = True)
        return render(request, self.template_name, locals())
    
    def post(request):
        pass
    
def liste(request, category ):
    cat = Product.objects.get(id= category)
    products = Product.objects.filter(active = True, categories = category)
    #pdr =  Product.objects.get(name=products)
    print(products)
    return render(request, "pages/categories.html" , locals())
    
def contact(request):
    site = Site_Info.objects.filter().first()
    return render(request, "pages/contact.html", locals())
    
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

def news_letter(request):
    msg =''
    success = True
    if request.method == "POST":
        email = request.POST.get("email")
        
        contact = NewsLetter( 
            email = email, 
        )
        
        contact.save()
        msg = 'Un message NewsLtters Success'
        
        data = {
        'msg': msg,
        'success': success
        }
        
    return JsonResponse(data, safe=False)
    
    
class ShopSingle(View):
    template_name = 'pages/single.html'
    
    def get(self,request, details): 
        products = Product.objects.get(id=details)
        return render(request, self.template_name, locals())
    
    def post(self, request):
        pass
    

        

