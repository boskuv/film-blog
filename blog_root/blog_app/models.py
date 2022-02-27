from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class Actor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='actors/', blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Film(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    image = models.ImageField(upload_to='films/', blank=True)

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        return self.film.all().aggregate(Avg('rate')).get('rate__avg', 0.00)


class Rating(models.Model):
    rate = models.PositiveSmallIntegerField(blank=True, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film')
