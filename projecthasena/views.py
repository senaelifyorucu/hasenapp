from django.http.response import HttpResponse
from django.shortcuts import render
from projecthasena.models import Blog, Category

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "projecthasena/index.html", context)

def blogs(request):
    return render(request, "projecthasena/blogs.html")

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "projecthasena/blog-details.html", {
        "blog": blog
    })

def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "projecthasena/blogs.html", context)