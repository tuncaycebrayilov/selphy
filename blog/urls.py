from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.Blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail')
]