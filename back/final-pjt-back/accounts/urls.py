from django.urls import path, include
from . import views

urlpatterns = [
    path('user/<int:user_pk>/', views.user_info),
    path('user/remove/<int:user_pk>/', views.user_delete),
    path('user/follow/<int:followed_pk>/<int:following_pk>/', views.user_follow),
    path('user/<int:user_pk>/likemovies/', views.user_like_movie),
]