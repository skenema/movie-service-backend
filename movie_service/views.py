from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
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

# TODO: Authenticate the request
@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_movie(request):
    title = request.data['title']
    cinema = request.data['cinema']
    description = request.data['description']
    # TODO: Handle file later
    movie = Movie.objects.create(title=title, cinema=cinema, description=description)
    # thumbnail = request.data['thumbnail']

    # Note: I think movies service might need to send something to reservation service here.
    # The alternate solution is to allow create showtime independently but that is not consistent.
    # - Pontakorn Paesaeng
    return Response({
        "id": movie.id,
        "title": movie.title,
        "description": movie.description,
        "cinema": movie.cinema
    })