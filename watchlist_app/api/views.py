from rest_framework.response import Response 
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view()
def watch_list(request):
  movies=Movie.objects.all()
  serializer=MovieSerializer(movies)
  return Response(serializer.data)


# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def watch_list(request):
#   movies = Movie.objects.all()
#   data = {
#    'movies': list(movies.values()),
#   }
  
#   return JsonResponse(data)

# def movie_detail(request, pk):
#   movie_detail = Movie.objects.get(pk=pk)
#   data = {
#     'title': movie_detail.title,
#     'description': movie_detail.description,
#     'active': movie_detail.active
#   }
  
#   return JsonResponse(data)