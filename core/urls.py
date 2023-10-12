from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.Message, name='contact'),
    path('index/', views.index, name='index'),
]