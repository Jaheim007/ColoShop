from django.urls import path 
from . import views

urlpatterns = [
    path('verify', views.verification , name="verify" ),
    path('contact/', views.contact , name="contact" ),
    path('news_verify', views.news_letter, name="news_verify")
]
