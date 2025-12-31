from django.shortcuts import render

from app.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryFrom

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    form = CategoryFrom()
    
    context = {
        'form': form,
    }
    return render(request,'dashboard/add_category.html', context)