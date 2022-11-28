from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=200)

class Actor(models.Model):
    name = models.CharField(max_length=200)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(null=True)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    tmdb_id = models.IntegerField()