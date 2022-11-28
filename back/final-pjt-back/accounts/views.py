from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserProfileSerializer, UserUpdateSerializer, UserDeleteSerializer
from movies.serializers import MovieSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie

# Create your views here.
@api_view(['GET', 'PUT'])
def user_info (request, user_pk):
    if request.method == "GET":
        user = get_object_or_404(get_user_model(), pk=user_pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT":
        user = get_object_or_404(get_user_model(), pk=user_pk)
        serializer = UserUpdateSerializer(user, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def user_delete(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    user.delete()
    # serializer = UserDeleteSerializer(user, data = request.data)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save()
    return Response( status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_follow(request, followed_pk, following_pk):
    target = get_object_or_404(get_user_model(), pk=followed_pk)
    follower = get_object_or_404(get_user_model(), pk=following_pk)
    if following_pk != followed_pk:
        if target.followers.filter(pk=follower.pk).exists():
            target.followers.remove(follower)
        else:
            target.followers.add(follower)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def user_like_movie(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    like_movies = request.data['likemovies']
    Movies = Movie.objects.filter(id__in=like_movies)
    for i in Movies:
        if i.like_users.filter(pk=user_pk):
            i.like_users.remove(user)
        else:
            i.like_users.add(user)
    
    return Response(status=status.HTTP_202_ACCEPTED)