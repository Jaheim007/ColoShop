from Shop import models
from django.shortcuts import render

def home_category(request, category):
    category = models.Category.objects.get(id = category) 
    categories = models.Category.objects.filter(active=True)
    products = models.Product.objects.filter(active = True)
    return render(request, 'pages/categories.html', locals())

# Create your views here.
