from django.urls import path 
from . import views

urlpatterns = [
    path('verify', views.verification , name="verify" ),
    path('post_home', views.post_home , name ="post_home"),
    path('contact/', views.contact , name="contact" ),
    path('news_verify', views.news_letter, name="news_verify"), 
    path('shop_category/<int:category>/', views.liste, name= "shop_category"),
]
