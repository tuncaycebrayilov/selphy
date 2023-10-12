from django.contrib import admin

# Register your models here.

from .models import blog, Category, Author, Tag, Comment

admin.site.site_header = "Selphy panel"
admin.site.site_title = "Selphy"

class blogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'date']
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(blog, blogAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)