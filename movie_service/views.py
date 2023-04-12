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
