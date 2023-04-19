from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie


@api_view(['GET'])
def get_movies_detail(request):
    movies_object = Movie.objects.all()
    movies_detail = []
    for movie in movies_object:
        movies_detail.append({"id": movie.id,
                              "title": movie.title,
                              "description": movie.description,
                              "cinema": movie.cinema,
                              })
    return Response(movies_detail)

@api_view(['GET'])
def get_movie_reservation(request, movie_id):
    movies_object = Movie.objects.get(pk=int(movie_id))
    response = {"title": movies_object.title,
                "cinema": movies_object.cinema}
    return Response(response)


