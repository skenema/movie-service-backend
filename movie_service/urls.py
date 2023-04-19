from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies_detail),
    path('movie/<int:movie_id>/detail', views.get_movie_reservation)
]