from django.urls import path
from watchlist_app.api.views import stream_plataform_detail
# movies_list, movie_details
from watchlist_app.api.views import (MoviesListAV, MovieDetailAV,
                                     StreamPlataformAV, ReviewList,
                                     ReviewCreate, ReviewDetail)
# StreamPlataformDetailAV

urlpatterns = [
  path("movies/", MoviesListAV.as_view(), name="movies_list"),
  path("movies/<int:pk>/", MovieDetailAV.as_view(), name="movie_detail"),
  path("platform/", StreamPlataformAV.as_view(), name="platform"),
  path("platform/<int:pk>/", stream_plataform_detail, name="platform_detail"),

  # path("reviews/", ReviewList.as_view(), name="reviews"),
  # path("reviews/<int:pk>/", ReviewDetail.as_view(), name="reviews_detail")

  path("movies/<int:pk>/reviews/", ReviewList.as_view(), name="review_list"),
  path("movies/<int:pk>/review-create/", ReviewCreate.as_view(), name="review_create"),
  path("movies/<int:movie_pk>/reviews/<int:pk>/", ReviewDetail.as_view(), name="review_detail")
  # path("movies/<int:movie_pk>/reviews/<int:review_pk>/", ReviewDetail.as_view(), name="review_update")
  

  
  # path("stream/<int:pk>/", StreamPlataformDetailAV.as_view(), name="stream_detail"),
  # path("", movies_list, name="movie_list"),
  # path("<int:pk>/", movie_details, name="movie_details"),

]
