from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Review, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model
from .serializers import ReviewSerializer, ReviewListSerializer, CommentSerializer, MovieReviewSerializer

# 게시판 전체 가져오기, 전체에서 작성하기
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def community_list(request):
    if request.method == 'GET':
        reviews = Review.objects.order_by('-pk')
        print('GET나왔음!')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = ReviewSerializer(data=request.data)
    #     user = get_object_or_404(get_user_model(), pk=request.POST.get('user'))
    #     movie = get_object_or_404(Movie, pk=request.POST.get('movie'))
    #     if serializer.is_valid(raise_exception=True):
    #         print('POST나왔음!')
    #         serializer.save(user=user, movie=movie)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 특정 영화의 게시판 게시글 가져오기, 작성하기
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def movie_community_list(request, movie_pk):
  
  # movie_id 조건 어떻게 달아야 특정 영화 게시글만 나오게 하는지 모르겠
    if request.method == 'GET':
        print(111231241242134)
        print('GET나왔음!')
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieReviewSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        user = get_object_or_404(get_user_model(), pk=request.data['user'])
        movie = get_object_or_404(Movie, pk=movie_pk)
        # movie = get_object_or_404(Movie, pk=request.POST.get('movie'))
        if serializer.is_valid(raise_exception=True):
            print('POST나왔음!')
            serializer.save(user=user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def community_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        if not request.data['user'] or request.data['user'] != review.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
        

# 게시글 추천수(좋아요 개념)
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def review_recommended(request, review_pk, user_pk, movie_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # movie = get_object_or_404(Movie, pk=movie_pk)
    # user = get_object_or_404(get_user_model(), pk=request.POST.get('user'))
    # user_pk = request.POST.get('userPk')
    user = get_object_or_404(get_user_model(), pk=user_pk)

    if review.user.id != user_pk:
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            is_liked = False
        else:
            review.like_users.add(user)
            is_liked = True
        context = {
            'is_liked':is_liked,
            'review_like_users_count':review.like_users.count()
        }
        return JsonResponse(context)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# 여기서부터 댓글 기능
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def comment_list(request, review_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        print('댓글 GET')
        return Response(serializer.data)
    # 댓글 생성
    elif request.method == 'POST':
        # movie = get_object_or_404(Movie, pk=movie_pk)
        review = get_object_or_404(Review, pk=review_pk)
        user = get_object_or_404(get_user_model(), pk=request.data['user'])
        serializer = CommentSerializer(data=request.data)
        print('왓더퍽')
        if serializer.is_valid(raise_exception=True):
            if request.data['parent']:
                print('대댓글_진입')
                # userPk
                parent_comment = get_object_or_404(Comment, pk=request.data['parent'])
                serializer.save(review=review, parent_comment=parent_comment, user=user)
            else:
                print('그냥 댓글 진입')
                serializer.save(review=review, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk, review_pk):
  comment = get_object_or_404(Comment, pk=comment_pk)

  if request.method == 'GET':
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

  elif request.method == 'DELETE':
      comment.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

  elif request.method == 'PUT':
    print(request.data)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def comment_create(request, review_pk, parent_comment):
#     review = get_object_or_404(Review, pk=review_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       if request.POST.get('parent'):
#         print('대댓글_진입')
#         # userPk
#         parent_comment = get_object_or_404(Comment, pk=request.POST.get('parent'))
#         serializer.save(review=review, movie=movie, parent_comment=parent_comment)    

# @api_view(['GET','DELETE','PUT'])
# # @permission_classes([IsAuthenticated])
# def parent_comment(request, review_pk, parent_comment_pk, movie_pk):
#     # review = get_object_or_404(Review, pk=review_pk)
#     parent_comment = get_object_or_404(Comment, pk=parent_comment_pk)
#     if request.method == 'GET':
#       serializer = CommentSerializer(parent_comment)
#       return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#       parent_comment.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#       serializer = CommentSerializer(parent_comment, data=request.data)
#       if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(serializer.data)


