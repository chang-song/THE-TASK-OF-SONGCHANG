from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile, Favorite, Anime

admin.site.register(UserProfile)
admin.site.register(Favorite)
admin.site.register(Anime)
