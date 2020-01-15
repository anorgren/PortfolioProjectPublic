from django.shortcuts import render

from .models import Job

def home_page(request):
    """The view for the home page of the app"""
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
