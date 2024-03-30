from django.db import models
from django.contrib.auth.models import User


class Anime(models.Model):
    name = models.CharField(max_length=100)
    episodes = models.IntegerField()
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.django.core.exceptions.FieldError: Unknown field(s) (title) specified for Anime
# 番剧模型
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Anime, through='Favorite')

    def __str__(self):
        return self.user.username


class Favorite(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('want_to_watch', 'Want to Watch'),
        ('watched', 'Watched'),
        ('watching', 'Watching'),
        ('on_hold', 'On Hold'),
        ('dropped', 'Dropped'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user_profile.user.username} - {self.anime.name}'


class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_of')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.friend.username}'