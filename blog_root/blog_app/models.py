from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#class Meta
class Actor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to ='actors/')

    def __str__(self):
        return f'{self.name} {self.surname}'


class Film(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    rating = models.PositiveSmallIntegerField(blank=True, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    image = models.ImageField(upload_to ='films/')

    def __str__(self):
        return self.title
