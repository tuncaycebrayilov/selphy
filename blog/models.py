from django.db import models

# Create your models here.
from mysite.utils.base import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Author(BaseModel):
    image = models.ImageField(verbose_name='Image for your author')
    name = models.CharField(max_length=100)
    about = models.TextField(verbose_name='About the author')

    def __str__(self):
        return self.name
    
class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class blog(BaseModel):
    STATUS = ('Publish', 'Publish'),('Draft', 'Draft')


    title = models.CharField(max_length=255, verbose_name='Title of your blog', help_text='Max character limit 255')
    image = models.ImageField(verbose_name='Image for your blog')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category of your blog')
    desc = models.TextField(verbose_name='Your blog')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    status = models.CharField(choices=STATUS, max_length=200)
    tag = models.ManyToManyField(Tag, verbose_name='Tag of your blog')

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'All blogs'

    def __str__(self):
        return self.title
    

class Comment(BaseModel):
    blogs = models.ForeignKey(blog, related_name='comments', on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.blogs.title, self.commenter_name)