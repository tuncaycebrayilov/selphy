from django.shortcuts import render, redirect

from .models import *
from shop.models import *
from blog.models import blog
from shop.models import product_version
from .forms import LeaveMessageForm
import random
# Create your views here.


def index(request):
    blogs = blog.objects.order_by("-date").all()[:2]
    product = product_version.objects.order_by("-date").all()[:5]
    products = product_version.objects.all()
    context = {
        'blogs': blogs,
        'product': product,
        'products':products
    }
    return render(request, 'index.html', context=context)


def Message(request):
    context = {
        'form': LeaveMessageForm()
    }
    if request.method == 'POST':
        form = LeaveMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = LeaveMessageForm()
    
    return render(request, 'contact.html', context=context)