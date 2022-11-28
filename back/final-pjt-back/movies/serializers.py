from rest_framework import serializers
from .models import Movie, Genre, Actor
from community.serializers import ReviewListSerializer, ReviewSerializer


class GenreSerializer(serializers.ModelSerializer):

  class Meta:
    model = Genre
    fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
 
  class Meta:
    model = Actor
    fields = '__all__'
class MovieListSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)
    reviews = ReviewListSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
  actors = ActorSerializer(many=True)
  genres = GenreSerializer(many=True)
  review = ReviewSerializer(many=True)
  class Meta:
      model = Movie
      fields = '__all__'

class RecommendedMovieSerializer(serializers.ModelSerializer):
  actors = ActorSerializer(many=True)
  genres = GenreSerializer(many=True)
  
  class Meta:
        model = Movie
        fields = '__all__'
