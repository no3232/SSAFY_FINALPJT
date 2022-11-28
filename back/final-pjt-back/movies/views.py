from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Movie
from django.contrib.auth import get_user_model
from .serializers import MovieListSerializer, MovieSerializer, RecommendedMovieSerializer

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)[:500]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         # serializer.save(user=request.user)
    #         return Response(serializer.errors, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)

# 영화 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, user_pk):
    movie = get_object_or_404(Movie, pk=request.data['movie'])
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        # movie["like_users"].remove(user)
    else:
        movie.like_users.add(user)
        # movie["like_users"].append(user)
    return Response(status=status.HTTP_202_ACCEPTED)

# 좋아요 많은 장르 선택하기
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def favorite_genre(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    like_movies = user.like_movies.all()
    # 해당 영화와 같은 장르만
    like_dict = dict()
    for like_movie in like_movies:
        for genre in like_movie.genres.all():
            if genre.pk not in like_dict:
                like_dict[genre.pk] = 1
            else:
                like_dict[genre.pk] += 1
    # 사용자가 누른 좋아요 영화의 장르 카운팅해서 가장 많이 본 장르 정하고
    favorite_genre_num = max(like_dict,key=like_dict.get)
    print(favorite_genre_num)
    context = {
      'favorite_genre_num': favorite_genre_num
    }
    return Response(context, status=status.HTTP_202_ACCEPTED)

# (좋아요 누른 영화만)(회원만)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_movies(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    # 특정 userPk를 가지고있는 유저가 좋아요 누른 영화 가져오고
    like_movies = user.like_movies.all()
    serializer = MovieListSerializer(like_movies, many=True)
    return Response(serializer.data)

# 좋아요 누른 영화는 제외
# (좋아요 누른 장르 중에서) 평점 기준 영화 추천 알고리즘
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommended_vote_average(request, user_pk):
    movies = get_list_or_404(Movie)[:500]
    # userPk = request.POST.get('userPk')
    user = get_object_or_404(get_user_model(), pk=user_pk)
    # if user.is_authenticated:
    # 특정 userPk를 가지고있는 유저가 좋아요 누른 영화 가져오고
    like_movies = user.like_movies.all()
    # 해당 영화와 같은 장르만
    like_dict = dict()
    for like_movie in like_movies:
        for genre in like_movie.genres.all():
            if genre.pk not in like_dict:
                like_dict[genre.pk] = 1
            else:
                like_dict[genre.pk] += 1
    # 사용자가 누른 좋아요 영화의 장르 카운팅해서 가장 많이 본 장르 정하고
    max_movie_like = max(like_dict,key=like_dict.get)
    print(max_movie_like)
    # 그 장르에 해당하는 영화 다 가져오고
    recommend_movie_lst = []
    for movie in movies:
        for genre in movie.genres.all():
            if genre.pk == max_movie_like:
                recommend_movie_lst.append(movie)

    recommend_movie_sorted_lst = []
    for recommend_movie in recommend_movie_lst:
      # 추천영화가 좋아요 누른 영화에 속한다면, 제외
        if recommend_movie in like_movies:
          continue
        recommend_lst = []

        recommend_lst.append(recommend_movie.id),
        recommend_lst.append(recommend_movie.title),
        recommend_lst.append(recommend_movie.release_date),
        recommend_lst.append(recommend_movie.popularity),
        recommend_lst.append(recommend_movie.vote_count),
        recommend_lst.append(recommend_movie.vote_average),
        recommend_lst.append(recommend_movie.overview),
        recommend_lst.append(recommend_movie.poster_path),
        recommend_lst.append(recommend_movie.tmdb_id),
        recommend_lst.append(recommend_movie.genres.all()),
        recommend_lst.append(recommend_movie.like_users.all())
        recommend_lst.append(recommend_movie.actors.all())

        # 다 넣으면 배열에 넣기
        recommend_movie_sorted_lst.append(recommend_lst)
        recommend_movie_sorted_lst.sort(key=lambda x : (-x[5], -x[4]))

    recommend_movie_sorted_final_lst = []
    for recommend_movie in recommend_movie_sorted_lst:
        # 딕셔너리 초기화 
        recommend_dict = dict()

        recommend_dict["id"]=recommend_movie[0]
        recommend_dict["title"]=recommend_movie[1]
        recommend_dict["release_date"]=recommend_movie[2]
        recommend_dict["popularity"]=recommend_movie[3]
        recommend_dict["vote_count"]=recommend_movie[4]
        recommend_dict["vote_average"]=recommend_movie[5]
        recommend_dict["overview"]=recommend_movie[6]
        recommend_dict["poster_path"]=recommend_movie[7]
        recommend_dict["tmdb_id"]=recommend_movie[8]
        recommend_dict["genres"]=recommend_movie[9]
        recommend_dict["like_users"]=recommend_movie[10]
        recommend_dict["actors"]=recommend_movie[11]

        recommend_movie_sorted_final_lst.append(recommend_dict)

    serializer = RecommendedMovieSerializer(recommend_movie_sorted_final_lst[0:30], many=True)
    return Response(serializer.data)

# 좋아요 누른 영화는 제외
# (좋아요 누른 장르 중에서) 관객수 기준 영화 추천 알고리즘
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommended_vote_count(request, user_pk):
    movies = get_list_or_404(Movie)[:500]
    # userPk = request.POST.get('userPk')
    user = get_object_or_404(get_user_model(), pk=user_pk)
    # if user.is_authenticated:
    # 특정 userPk를 가지고있는 유저가 좋아요 누른 영화 가져오고
    like_movies = user.like_movies.all()
    # 해당 영화와 같은 장르만
    like_dict = dict()
    for like_movie in like_movies:
        for genre in like_movie.genres.all():
            if genre.pk not in like_dict:
                like_dict[genre.pk] = 1
            else:
                like_dict[genre.pk] += 1
    # 사용자가 누른 좋아요 영화의 장르 카운팅해서 가장 많이 본 장르 정하고
    max_movie_like = max(like_dict,key=like_dict.get)
    print(max_movie_like)
    # 그 장르에 해당하는 영화 다 가져오고
    recommend_movie_lst = []
    for movie in movies:
        for genre in movie.genres.all():
            if genre.pk == max_movie_like:
                recommend_movie_lst.append(movie)

    # print('+++++++++++++++++++++++++')

    recommend_movie_sorted_lst = []
    for recommend_movie in recommend_movie_lst:
      # 추천영화가 좋아요 누른 영화에 속한다면, 제외
        if recommend_movie in like_movies:
          continue
        recommend_lst = []

        recommend_lst.append(recommend_movie.id),
        recommend_lst.append(recommend_movie.title),
        recommend_lst.append(recommend_movie.release_date),
        recommend_lst.append(recommend_movie.popularity),
        recommend_lst.append(recommend_movie.vote_count),
        recommend_lst.append(recommend_movie.vote_average),
        recommend_lst.append(recommend_movie.overview),
        recommend_lst.append(recommend_movie.poster_path),
        recommend_lst.append(recommend_movie.tmdb_id),
        recommend_lst.append(recommend_movie.genres.all()),
        recommend_lst.append(recommend_movie.like_users.all())
        recommend_lst.append(recommend_movie.actors.all())


        # 다 넣으면 배열에 넣기
        recommend_movie_sorted_lst.append(recommend_lst)
        recommend_movie_sorted_lst.sort(key=lambda x : (-x[3], -x[4]))

    recommend_movie_sorted_final_lst = []
    for recommend_movie in recommend_movie_sorted_lst:
        # 딕셔너리 초기화 
        recommend_dict = dict()

        recommend_dict["id"]=recommend_movie[0]
        recommend_dict["title"]=recommend_movie[1]
        recommend_dict["release_date"]=recommend_movie[2]
        recommend_dict["popularity"]=recommend_movie[3]
        recommend_dict["vote_count"]=recommend_movie[4]
        recommend_dict["vote_average"]=recommend_movie[5]
        recommend_dict["overview"]=recommend_movie[6]
        recommend_dict["poster_path"]=recommend_movie[7]
        recommend_dict["tmdb_id"]=recommend_movie[8]
        recommend_dict["genres"]=recommend_movie[9]
        recommend_dict["like_users"]=recommend_movie[10]
        recommend_dict["actors"]=recommend_movie[11]


        recommend_movie_sorted_final_lst.append(recommend_dict)

    # for row in recommend_movie_sorted_final_lst:
    #   print(row)
    # print()

    # return render (request, 'movies/recommended.html', context)
    serializer = RecommendedMovieSerializer(recommend_movie_sorted_final_lst[0:30], many=True)
    return Response(serializer.data)

# (좋아요 누른 장르 중에서) 랜덤으로 추출(회원만)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def recommended_random(request, user_pk):
    movies = get_list_or_404(Movie)[:500]
    user = get_object_or_404(get_user_model(), pk=user_pk)
    # 특정 userPk를 가지고있는 유저가 좋아요 누른 영화 가져오고
    like_movies = user.like_movies.all()
    # 해당 영화와 같은 장르만
    like_dict = dict()
    for like_movie in like_movies:
        for genre in like_movie.genres.all():
            if genre.pk not in like_dict:
                like_dict[genre.pk] = 1
            else:
                like_dict[genre.pk] += 1
    # 사용자가 누른 좋아요 영화의 장르 카운팅해서 가장 많이 본 장르 정하고
    max_movie_like = max(like_dict,key=like_dict.get)

    print(max_movie_like)

    # 그 장르에 해당하는 영화 다 가져오고
    recommend_movie_lst = []
    for movie in movies:
        for genre in movie.genres.all():
            if genre.pk == max_movie_like:
                recommend_movie_lst.append(movie)

    random_movie_lst = []
    for recommend_movie in recommend_movie_lst:
    # 추천영화가 좋아요 누른 영화에 속한다면, 제외
        if recommend_movie in like_movies:
            continue
        random_movie_lst.append(recommend_movie)

    random_lst = random.sample(recommend_movie_lst, 12)
    serializer = RecommendedMovieSerializer(random_lst[0:30], many=True)
    return Response(serializer.data)