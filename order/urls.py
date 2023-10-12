from django.urls import path
from . import views


urlpatterns = [
    path('cart/', views.shopping_cart_vews, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist_views, name='wishlist')
]