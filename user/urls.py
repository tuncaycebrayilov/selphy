from django.urls import path
from .views import RegisterView, CustomLoginView, activate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('logout/', LogoutView.as_view(), name='logout'),
]