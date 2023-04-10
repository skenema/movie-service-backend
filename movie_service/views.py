from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movies, ShowTimes

@api_view(['GET'])
def get_movies_detail(request):
    if request.method == 'GET':
        movies_object = Movies.objects.all()
        movies_detail = []
        for movie in movies_object:
            time_list = []
            show_time_object = ShowTimes.objects.filter(movies=movie.id)
            for time in show_time_object:
                time_list.append({  "id": time.id,
                                    "start_time": time.start_time})
            
            movies_detail.append({  "id": movie.id,
                                    "title": movie.title,
                                    "description": movie.description,
                                    "cinema": movie.cineme,
                                    "showtimes": time_list
            })
        return Response(movies_detail)