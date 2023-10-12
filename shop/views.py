from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import *
from .forms import ReviewForm



def shop(request):
    allproduct = product_version.objects.order_by('-created').distinct()
    manufacturer = Manufacturer.objects.all()
    color = Color.objects.all()
    tag = Tag.objects.all()
    category = Category.objects.all()

    p = Paginator(product_version.objects.all(), 4)
    page = request.GET.get('page')
    page_number = p.get_page(page)

    manufacturer_id = request.GET.get('manufacturer')
    color_id = request.GET.get('color')
    tags_id = request.GET.get('tag')
    category_id = request.GET.get('category')

    if color_id:
        page_number = product_version.objects.filter(color = color_id)
    elif manufacturer_id:
        page_number = product_version.objects.filter(product__manufacturer = manufacturer_id)
    elif tags_id:
        page_number = product_version.objects.filter(product__tag = tags_id)
    elif category_id:
        page_number = product_version.objects.filter(product__category = category_id)
    else:
        allproduct = product_version.objects.all()

    context = {
        'all' : allproduct,
        'manufacturer': manufacturer,
        'color' : color,
        'tag' : tag,
        'category': category,
        'page_number': page_number
    }
    return render(request, 'shop.html', context=context)





def product_details(request, pk):
    products = product_version.objects.filter(pk=pk).first()
    reviews = Review.objects.filter(products__pk=pk).all()
    tags = Tag.objects.all()
    image = Image.objects.all()
    colors = Color.objects.all()
    product_colors = []
    for color in colors:
        if products.product.pk == color.product_color.first().product.pk:
            product_colors.append({'color': color, 'pk': color.product_color.all().first().pk})
    print(product_colors)
    
    form = ReviewForm()

    color_id = request.GET.get('color')
    tags_id = request.GET.get('tags')

    if tags_id:
        products = Tag.objects.filter(tag = tags_id)
    elif color_id:
        products = Color.objects.filter(color = color_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.products = products
            review.save()
            return redirect('product_details', pk=pk)
    else:
        form = ReviewForm()

    context = {
        'product': products,
        'reviews': reviews,
        'form': form,
        'tags' : tags,
        'image': image,
        'colors': product_colors
        
    }
    return render(request, 'product-details.html', context=context)



@login_required(login_url='login')
def wishlist_view(request, pk):
    product = product_version.objects.get(id=pk)
    choosen, created = Wishlist.objects.get_or_create(user = request.user, product=product)

    if not created:
        choosen.quantity += 1
        choosen.save()
    return redirect('shop')

@login_required(login_url='login')
def add_to_cart(request, pk):
    product = product_version.objects.get(id=pk)
    cart, created = Add_to_Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart.quantity += 1
        cart.save()
    return redirect('shop')


@login_required(login_url='login')
def remove_wishlist_product(request, pk):
    product = get_object_or_404(product_version, id = pk)
    print(product)
    try:
        cart_items = Wishlist.objects.filter(user = request.user, product = product)
        product.save()
        cart_items.delete()
    except Wishlist.DoesNotExist:
        pass

    return redirect('wishlist')

@login_required(login_url='login')
def remove_cart_product(request, pk):
    product = get_object_or_404(product_version, id = pk)

    try:
        cart_items = Add_to_Cart.objects.filter(user = request.user, product = product)
        product.save()
        cart_items.delete()
    except Add_to_Cart.DoesNotExist:
        pass

    return redirect('cart')