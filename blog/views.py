from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category
from .models import *

def Home(request):
    template_name = 'home.html'
    posts = BlogPost.objects.filter(status='published').order_by('-created')
    context = {'posts': posts}
    return render(request, template_name, context)

def Blog(request):
    queryset = BlogPost.objects.filter(status='published').order_by('-created')
    per_page = 3
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    template_name = 'Blog/blog.html'
    context = {'posts': posts}
    return render(request, template_name, context)

def single_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    template_name = 'Blog/single.html'
    context = {'post': post}
    return render(request, template_name, context)


def category_page(request, category_slug):
    categori = Category.objects.get(slug=category_slug)
    category_list = Category.objects.all() 
    context={'categori':categori,'category': category_list,}
    return render(request,'blog/category_details.html',context)

def handler404(request, exception):
    return render(request, '404.html', status=404)