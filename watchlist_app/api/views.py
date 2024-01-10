from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

class MoviesListAV(APIView):
  def get(self, request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer=MovieSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class MovieDetailAV(APIView):
  def get(self, request, pk):
    try:
      movie=Movie.objects.get(pk=pk)
      serializer=MovieSerializer(movie)
      return Response(serializer.data)
    except Movie.DoesNotExist:
      return Response ({'error: movie not found'}, status=status.HTTP_404_NOT_FOUND) 

  def put(self, request, pk):
    movie=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response('registro actualizado', status=status.HTTP_202_ACCEPTED)
    else:
      return Response(serializer.errors)    

  def delete(self, request, pk):
    movie=Movie.objects.get(pk=pk)
    movie.delete()
    return Response('registro eliminado', status=status.HTTP_202_ACCEPTED)



# @api_view(['GET', 'POST'])
# def movies_list(request):
#   if request.method == 'GET':
#     movies=Movie.objects.all()
#     serializer=MovieSerializer(movies, many=True)
#     return Response(serializer.data)
  
#   elif request.method == 'POST':
#     serializer=MovieSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#   if request.method == 'GET':
#     try:
#       movie=Movie.objects.get(pk=pk)
#       serializer=MovieSerializer(movie)
#       return Response(serializer.data)
#     except Movie.DoesNotExist:
#       return Response({'Error': 'movie not found'}, status=status.HTTP_404_NOT_FOUND ) 
  
#   elif request.method == 'PUT':
#     movie=Movie.objects.get(pk=pk)
#     serializer=MovieSerializer(movie, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response('registro actualizado', status=status.HTTP_202_ACCEPTED)
#     else:
#       return Response(serializer.errors)    

#   elif request.method == 'DELETE':
#     movie=Movie.objects.get(pk=pk)
#     movie.delete()
#     return Response('Registro elimininado', status=status.HTTP_202_ACCEPTED)

  



  
  



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

