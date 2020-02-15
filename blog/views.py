from django.shortcuts import render
from blog.models import Blog

def allblogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/allblogs.html', {'blogs': blogs})