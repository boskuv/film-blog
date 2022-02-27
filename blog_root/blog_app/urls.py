from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('actor/<int:id>/', views.actor_detail, name='actor_detail'),
    path('rate_film/<int:id>/', views.rate_film_form, name="rate_film_form"),
]
