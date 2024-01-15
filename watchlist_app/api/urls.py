from django.urls import path
from watchlist_app.api.views import stream_plataform_detail
# movies_list, movie_details
from watchlist_app.api.views import MoviesListAV, MovieDetailAV, StreamPlataformAV 
# StreamPlataformDetailAV

urlpatterns = [
  path("", MoviesListAV.as_view(), name="movies_list"),
  path("<int:pk>/", MovieDetailAV.as_view(), name="movie_detail"),
  path("stream/", StreamPlataformAV.as_view(), name="stream"),
  path("stream/<int:pk>/", stream_plataform_detail, name="stream_detail"),
  # path("stream/<int:pk>/", StreamPlataformDetailAV.as_view(), name="stream_detail"),
  # path("", movies_list, name="movie_list"),
  # path("<int:pk>/", movie_details, name="movie_details"),

]
