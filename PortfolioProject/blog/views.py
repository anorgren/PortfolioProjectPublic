from django.shortcuts import render

from .models import Blog


def all_blogs(request):
    """Returns all blog posts"""
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})
