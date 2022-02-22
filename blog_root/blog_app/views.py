from django.shortcuts import render

def show_films(request):
    return render(request, 'blog_app/films.html', {})

def index(request):
    return render(request, 'blog_app/index.html', {})
