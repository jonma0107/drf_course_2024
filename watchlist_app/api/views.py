from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from rest_framework.exceptions import ValidationError

from rest_framework import permissions

from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly

from watchlist_app.models import Movie, StreamPlataform, Review
from watchlist_app.api.serializers import (
  MovieSerializer, StreamPlataformSerializer, ReviewSerializer)


# Stream Class

# ViewSet class
class StreamPlatform(viewsets.ModelViewSet):
  queryset = StreamPlataform.objects.all()
  serializer_class = StreamPlataformSerializer
  permission_classes = [permissions.IsAdminUser]
  

# class StreamPlataformAV(APIView):
#   def get(self, request):
#     stream = StreamPlataform.objects.all()
#     serializer = StreamPlataformSerializer(stream, many=True)
#     return Response(serializer.data)

#   def post(self, request):
#     serializer = StreamPlataformSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#       return Response(
#           serializer.errors,
#           status=status.HTTP_406_NOT_ACCEPTABLE)


# @api_view(['GET', 'PUT', 'DELETE'])
# def stream_plataform_detail(request, pk):
#   # consulta (queryset)
#   stream = StreamPlataform.objects.filter(id=pk).first()
#   # validación
#   if stream:
#     if request.method == 'GET':
#       serializer = StreamPlataformSerializer(stream)
#       return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'PUT':
#       serializer = StreamPlataformSerializer(stream, data=request.data)
#       if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#       else:
#         return Response(
#             serializer.errors,
#             status=status.HTTP_406_NOT_ACCEPTABLE)

#     elif request.method == 'DELETE':
#       stream.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)

#   else:
#     return Response(
#         {'error: stream not found'},
#         status=status.HTTP_404_NOT_FOUND)


# Movies Class
  
class MoviesListAV(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)    
    return Response(serializer.data)

  def post(self, request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(
          serializer.errors,
          status=status.HTTP_406_NOT_ACCEPTABLE)


class MovieDetailAV(APIView):

  permission_classes = [AdminOrReadOnly]

  def get(self, request, pk):
    try:
      movie = Movie.objects.filter(id=pk).first()
      if movie is not None:
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
      else:
        return Response(
            {'error: movie not found'},
            status=status.HTTP_404_NOT_FOUND)
    except Movie.DoesNotExist:
      return Response(
          {'error: movie not found'},
          status=status.HTTP_404_NOT_FOUND)

    # try:
    #   movie=Movie.objects.get(pk=pk)
    #   serializer=MovieSerializer(movie)
    #   return Response(serializer.data)
    # except Movie.DoesNotExist:
    #   return Response ({'error: movie not found'},
    #   status=status.HTTP_404_NOT_FOUND)

  def put(self, request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response('registro actualizado', status=status.HTTP_202_ACCEPTED)
    else:
      return Response(
          serializer.errors,
          status=status.HTTP_406_NOT_ACCEPTABLE)

  def delete(self, request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return Response('registro eliminado', status=status.HTTP_202_ACCEPTED)


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


# Review Class

# class ReviewList(
#   mixins.ListModelMixin,
#   mixins.CreateModelMixin,
#         generics.GenericAPIView):
#   queryset = Review.objects.all()
#   serializer_class = ReviewSerializer

#   def get(self, request, *args, **kwargs):
#     return self.list(request, *args, **kwargs)

#   def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)

# class ReviewList(generics.ListCreateAPIView):
#   queryset = Review.objects.all()
#   serializer_class = ReviewSerializer

  # Concrete View Classes

class ReviewList(generics.ListAPIView):

  permission_classes = [permissions.IsAuthenticated]
  serializer_class = ReviewSerializer

  def get_queryset(self):
    pk = self.kwargs['pk']
    return Review.objects.filter(movie=pk)


class ReviewCreate(generics.CreateAPIView):
  serializer_class = ReviewSerializer

  def get_queryset(self):
        return Review.objects.all()

  def perform_create(self, serializer):
    pk = self.kwargs.get('pk')
    movie = Movie.objects.get(pk=pk)    

    # Validar Usuario
    reviewer = self.request.user
    reviewer_queryset = Review.objects.filter(movie=movie, reviewer=reviewer)
    if reviewer_queryset.exists():
      raise ValidationError("Tu ya has reseñado esta película") 

    serializer.save(movie=movie, reviewer=reviewer)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [ReviewUserOrReadOnly]
  serializer_class = ReviewSerializer

  def get_queryset(self):
        return Review.objects.all()
  
  # def perform_update(self, serializer):
  #    pk=self.kwargs.get('pk')
  #    review=Review.objects.get(pk=pk)
     
  #    reviewer = self.request.user
  #    reviewer_queryset = Review.objects.filter(reviewer=reviewer)
  #    if reviewer_queryset.exists():
      
  #     # raise ValidationError("Tu ya has reseñado esta película antes") 

  #     serializer.save(review=review, reviewer=reviewer)
      


# class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
#   serializer_class = ReviewSerializer
#   queryset = Review.objects.all()
#   lookup_url_kwarg = 'review_pk'

#   def perform_update(self, serializer):
#     review_pk = self.kwargs.get('review_pk')
#     review_instance = Review.objects.get(pk=review_pk)
#     serializer.save(movie=review_instance.movie)
      

  # MIXIN'S

# class ReviewDetail(
#   mixins.RetrieveModelMixin,
#   mixins.UpdateModelMixin,
#   mixins.DestroyModelMixin,
#         generics.GenericAPIView):
#   queryset = Review.objects.all()
#   serializer_class = ReviewSerializer

#   def get(self, request, *args, **kwargs):
#     return self.retrieve(request, *args, **kwargs)

#   def put(self, request, *args, **kwargs):
#     return self.update(request, *args, **kwargs)

#   def delete(self, request, *args, **kwargs):
#     return self.destroy(request, *args, **kwargs)
