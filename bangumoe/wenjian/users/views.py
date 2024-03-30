from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .models import Anime, Favorite
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Friendship


def anime_list(request):
    anime = Anime.objects.all()
    return render(request, 'anime_list.html', {'anime': anime})


def add_to_favorites(request, anime_id):
    user_profile = request.user.userprofile
    anime = Anime.objects.get(id=anime_id)
    favorite, created = Favorite.objects.get_or_create(user_profile=user_profile, anime=anime)
    favorite.status = 'want_to_watch'
    favorite.save()
    return redirect('anime_list')


def update_status(request, favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)
    favorite.status = request.POST['status']
    favorite.save()
    return redirect('favorites')


def add_rating(request, favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)
    favorite.rating = request.POST['rating']
    favorite.save()
    return redirect('favorites')


def add_comment(request, favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)
    favorite.comment = request.POST['comment']
    favorite.save()
    return redirect('favorites')


def favorites(request):
    user_profile = request.user.userprofile
    favorites = Favorite.objects.filter(user_profile=user_profile)
    return render(request, 'favorites.html', {'favorites': favorites})


@login_required
def delete_friend(request, friend_id):
    user = request.user
    friend = User.objects.get(id=friend_id)
    Friendship.objects.filter(user=user, friend=friend).delete()
    return HttpResponseRedirect(reverse('my_friends'))


@login_required
def add_friend(request, friend_id):
    user = request.user
    friend = User.objects.get(id=friend_id)
    Friendship.objects.create(user=user, friend=friend)
    return HttpResponseRedirect(reverse('my_friends'))


@login_required
def friend_request(request):
    user = request.user
    friend_requests = Friendship.objects.filter(friend=user)
    return render(request, 'friend_request.html', {'friend_requests': friend_requests})


@login_required
def my_friends(request):
    user = request.user
    friends = Friendship.objects.filter(user=user)
    return render(request, 'my_friends.html', {'friends': friends})