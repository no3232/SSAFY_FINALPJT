from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model
# from movies.serializers import MovieListSerializer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)

class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie','user',)

class ChildCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)

class CommentSerializer(serializers.ModelSerializer):
    childcomment = ChildCommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review','movie',)


class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('comment_set', 'comment_count','movie','user',)
        # read_only_fields = (

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('reviews', )

# class CommentListSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Comment
#         fields = '__all__'
