from django.shortcuts import render,redirect,get_object_or_404

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

# add category

def add_category(request):
    form = CategoryFrom()
    if request.method == "POST":
        form = CategoryFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    context = {
        'form': form,
    }
    return render(request,'dashboard/add_category.html', context)

# delete category

def edit_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryFrom(instance=category)
    
    if request.method == "POST":
        form = CategoryFrom(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)
    
    
# delete catefory    
    
def delete_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')