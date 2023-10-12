from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogApiView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', views.BlogApiView.as_view(), name='blog'),
    path('products/', views.ShopApiView.as_view(), name='products'),
    path('products/<int:pk>/', views.ShopApiView.as_view(), name='product')
]