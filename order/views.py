from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import Wishlist, Add_to_Cart
# Create your views here.

@login_required(login_url='login')
def shopping_cart_vews(request):
    cartproducts = []
    if request.user.is_authenticated:
        user = request.user
        cartproducts = Add_to_Cart.objects.filter(user=user)

    return render(request, 'cart.html', {'cartproducts' : cartproducts})

def checkout(request):
    return render(request, 'checkout.html')

@login_required(login_url='login')
def wishlist_views(request):
    wishlist_products = []
    if request.user.is_authenticated:
        user = request.user
        wishlist_products = Wishlist.objects.filter(user=user)
    context = {
        'wishlists' : wishlist_products
    }

    return render(request, 'wishlist.html', context=context)


