from django.contrib import admin
from .models import Actor, Film, Rating

admin.site.register([Actor, Film, Rating])
