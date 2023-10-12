from django.urls import path
from . import views


urlpatterns = [
    path('shop/', views.shop, name='shop'),  
    path('productdetails/<int:pk>/', views.product_details, name='product_details'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('wishlist_view/<int:pk>/', views.wishlist_view, name='wishlist_view'),
    path('deletewishlist/<int:pk>/', views.remove_wishlist_product, name='remove_wishlist_product'),
    path('deletecart/<int:pk>/', views.remove_cart_product, name='remove_cart_product')
]