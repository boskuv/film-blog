from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Film, Actor, Rating
from .forms import RatingForm


def index(request):
    films = Film.objects.all()
    context = {
        'films': films,
        'form': RatingForm()
    }
    return render(request, 'blog_app/index.html', context)


def actor_detail(request, id):
    actor_instance = Actor.objects.get(id=id)
    films = Film.objects.filter(actors=actor_instance)
    context = {
        'actor': actor_instance,
        'films': films
    }
    return render(request, 'blog_app/actor.html', context)


def rate_film_form(request, id):
    if request.POST:
        rate_value = request.POST.get('rate')
        film_instance = Film.objects.get(id=id)
        Rating.objects.create(rate=rate_value, film=film_instance)
        return HttpResponseRedirect('/')
