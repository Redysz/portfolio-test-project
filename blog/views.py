from django.shortcuts import render
from blog.models import Blog

def allblogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
