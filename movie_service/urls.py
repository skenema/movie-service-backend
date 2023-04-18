from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies_detail),
    path('movies/create', views.create_movie)
]