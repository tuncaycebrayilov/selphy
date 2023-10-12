from django.shortcuts import render, redirect, get_object_or_404

from .models import blog, Category, Author, Tag, Comment
from .forms import CommentsForm
from datetime import datetime
from django.http import JsonResponse
from django.core.paginator import Paginator


def Blog(request):
    allblogs = blog.objects.order_by('-created').distinct()
    categories = Category.objects.all()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    recent_posts = blog.objects.order_by('date')[:5]
    recent_comments = Comment.objects.order_by('date_added')[:5]

    p = Paginator(blog.objects.all(), 4)
    page = request.GET.get('page')
    page_number = p.get_page(page)
    
    author_id = request.GET.get('authors')
    category_id = request.GET.get('categories')
    tags_id = request.GET.get('tags')

    if category_id:
        page_number = blog.objects.filter(category=category_id)
    elif author_id:
        page_number = blog.objects.filter(author = author_id)
    elif tags_id:
        page_number = blog.objects.filter(tag = tags_id)
    else:
        allblogs = blog.objects.filter(status='Publish')

    context = {
        'all' : allblogs,
        'recent_posts': recent_posts,
        'categories': categories,
        'authors' : authors,
        'tags' : tags,
        'recent_comments' : recent_comments,
        'page_number': page_number,
    }
    return render(request, 'blog.html', context=context)


def blog_detail(request, pk):
    blogs = blog.objects.filter(pk=pk).first()
    recent_posts = blog.objects.order_by('date')[:5]
    comments = Comment.objects.filter(blogs__pk=pk).all()
    recent_comments = Comment.objects.order_by('date_added')[:5]
    form = CommentsForm()

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blogs = blogs
            comment.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = CommentsForm()

    comments_count = Comment.objects.filter(blogs=blogs).count() 

    context = {
        'blog': blogs,
        'recent_posts': recent_posts,
        'comments': comments,
        'form' : form,
        'recent_comments' : recent_comments,
        'comments_count': comments_count
    }
    return render(request, 'blog-details.html', context=context)