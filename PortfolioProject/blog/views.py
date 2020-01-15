from django.shortcuts import render, get_object_or_404

from .models import Blog


def all_blogs(request):
    """Returns all blog posts"""
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    """Returns a detailed view of a blog post of a given id"""
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detail_blog})
