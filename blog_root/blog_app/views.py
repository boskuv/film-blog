from django.shortcuts import render
from .models import Film, Actor


def index(request):
    films = Film.objects.all()
    context = {
        'films': films
    }
    return render(request, 'blog_app/index.html', context)
