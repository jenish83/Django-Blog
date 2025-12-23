from django.shortcuts import render
from app.models import Category,Blog

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True , status=1).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status=1)
    
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
    }
    print(categories)
    return render(request, 'home.html', context)
    