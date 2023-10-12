from django.contrib import admin
from .models import product, Color, Manufacturer, Tag, Review, product_version, Image, Category, Add_to_Cart, Wishlist
from django.utils.html import format_html

class productModels(admin.ModelAdmin):
    list_display = ['title', 'price', 'desc', 'availability', 'manufacturer', 'category']
    list_filter = ['availability']
    search_fields = ['title']
    fieldsets = (
        ("General info", {"fields": ('title', 'desc', 'manufacturer', 'category')}),
        ("Detail info", {"fields": ('price', 'availability', 'tag')})
    )

class product_versionModels(admin.ModelAdmin):
    list_display = ['color', 'give_image', 'images', 'product']

    def give_image(self, obj):
        if obj.images:
            img = '<img src="{url}" width="200px" />'.format(url=obj.images.url) 
            print(img)
            return format_html(img)
        return format_html('<b style="color:black">No image</b>')



admin.site.register(product, productModels)
admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(product_version)
admin.site.register(Review)
admin.site.register(Manufacturer)
admin.site.register(Add_to_Cart)
admin.site.register(Wishlist)