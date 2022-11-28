from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:user_pk>/like/', views.movie_like),
    path('<int:user_pk>/like_movies/', views.like_movies),
    path('<int:user_pk>/favorite_genre/', views.favorite_genre),
    path('<int:user_pk>/recommended_vote_average/', views.recommended_vote_average),
    path('<int:user_pk>/recommended_vote_count/', views.recommended_vote_count),
    path('<int:user_pk>/recommended_random/', views.recommended_random),
]