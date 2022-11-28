from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_list),
    path('movie/<int:movie_pk>/', views.movie_community_list),
    path('movie/<int:movie_pk>/review/<int:review_pk>/', views.community_detail),
    path('movie/<int:movie_pk>/review/<int:review_pk>/review_recommended/<int:user_pk>/', views.review_recommended),
    path('review/<int:review_pk>/comments/', views.comment_list),
    path('review/<int:review_pk>/comments/<int:comment_pk>/', views.comment_detail),
]
