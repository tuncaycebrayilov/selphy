from django.db import models

from user.models import User
from mysite.utils.base import BaseModel

class Color(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Manufacturer(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(BaseModel):
    image = models.ImageField(max_length=100)

    def __str__(self):
        return f'{self.pk}'

class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class product(BaseModel):
    AVAILABILITY = (('In stock', 'In stock'), ('Out of stock', 'Out of stock'))

    title = models.CharField(max_length=255, verbose_name='Title of your product', help_text='Max character limit 255')
    price = models.IntegerField()
    desc = models.TextField(verbose_name='Your description')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Manufacturer')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    availability = models.CharField(choices=AVAILABILITY)
    tag = models.ManyToManyField(Tag, verbose_name='Tag of your product')

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'All products'

    def __str__(self):
        return self.title



class product_version(BaseModel):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="product_color")
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name="product_version")
    images = models.ManyToManyField(Image, related_name='images_of_products')
    cover_image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    def __str__(self):
        return f"{self.product.title}'s {self.color.name} version"
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(product_version, on_delete=models.CASCADE, related_name='product_wishlist')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'

    def str(self):
        return self.product.product.title


class Add_to_Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='add_to_cart')
    product = models.ForeignKey(product_version, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    class Meta:
        verbose_name = 'Add to Cart'
        verbose_name_plural = 'Add to Carts'

    def str(self):
        return self.product.product.title


class Review(BaseModel):
    Rates = {
        (1, "20"),
        (2, "40"),
        (3, "60"),
        (4, "80"),
        (5, "100")
    }

    products = models.ForeignKey(product_version, related_name='Reviews', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=200)
    review = models.TextField()
    price_review = models.IntegerField(choices=Rates)
    value_review = models.IntegerField(choices=Rates)
    quality_review = models.IntegerField(choices=Rates)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.products.product.title, self.nickname)
    
    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"