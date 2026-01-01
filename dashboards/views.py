from django.shortcuts import render,redirect,get_object_or_404

from app.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryFrom, BlogPostForm
from django.template.defaultfilters import slugify

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


def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts, 
    }
    return render(request, 'dashboard/posts.html', context)

def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # temporarily saving the form
            post.author = request.user
            post.save() 
            title = form.cleaned_data['title']
            # here after giving the slugify function it will give unique primary key ,
            # so we can add same content in slug but it will give unique id to each
            post.slug = slugify(title) + '-' +str(post.id)  
            post.save() 
            return redirect('posts')
        else:
            print("Form is invalid")
            print(form.errors)
    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request,'dashboard/add_post.html', context)

def edit_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES , instance=post)
        if form.is_valid():
            post = form.save()
            # while editing there might be some changes in the title so we have to add slugify here
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')

    form = BlogPostForm(instance=post)
      
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)
    
def delete_post(request,pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()  
    return redirect('posts')
    
