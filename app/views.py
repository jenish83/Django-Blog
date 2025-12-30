from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Blog,Category
from django.db.models import Q

# Create your views here.

def posts_by_category(request,category_id):
    # fetch the posts that belongs to the category with category id
    posts = Blog.objects.filter(status=1, category=category_id) 
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect user to the home page
    #     return redirect('home')
    # user get_object_or_404 when you want to show 404 error page if the category does not exists
    category = get_object_or_404(Category, pk=category_id)  
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)

def blogs(request,slug):
    single_blog = get_object_or_404(Blog, slug=slug, status=1)
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    
    # Q allows complex database queries using OR, AND, and NOT logic by using |, &, and ~.
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status=1)
    
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html',context)