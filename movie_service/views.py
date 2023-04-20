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

@api_view(['GET'])
def get_movie_reservation(request, movie_id):
    movies_object = Movie.objects.get(pk=int(movie_id))
    response = {"title": movies_object.title,
                "cinema": movies_object.cinema}
    return Response(response)



# TODO: Authenticate the request
@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_movie(request):
    title = request.data['title']
    cinema = request.data['cinema']
    description = request.data['description']
    thumbnail = request.data['thumbnail']
    # TODO: Handle file later
    # Please also note lack of validation here.
    # We don't have logic to validate anything yet
    # - Pontakorn Paesaeng
    movie = Movie.objects.create(title=title, cinema=cinema, description=description, thumbnail=thumbnail)

    # Note: I think movies service might need to send something to reservation service here.
    # The alternate solution is to allow create showtime independently but that is not consistent.
    # - Pontakorn Paesaeng
    return Response({
        "id": movie.id,
        "title": movie.title,
        "description": movie.description,
        "cinema": movie.cinema,
        "thumbnail":  movie.thumbnail.url if movie.thumbnail else ""
    })