from django.urls import path 
from . import views
from Cart import views as cart
from Cart.views import Cart

urlpatterns = [
    path('verify', views.verification , name="verify" ),
    # path('post_home', views.post_home , name ="post_home"),
    path('contact/', views.contact , name="contact" ),
    path('news_verify', views.news_letter, name="news_verify"), 
    path('shop_category/<int:category>/', views.liste, name= "shop_category"),
    path("cart/", Cart , name="cart"),
    path("add_to_cart/<int:product_id>/", cart.add_cart,  name="add_to_cart" ),
    path("remove_item/<int:product_id>/", cart.remove_item, name="remove_item")
]
