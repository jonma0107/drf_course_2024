from django.urls import path
from watchlist_app.api.views import movies_list, movie_details

urlpatterns = [
  path("", movies_list, name="movie_list"),
  path("<int:pk>/", movie_details, name="movie_details"),
#   path("update/<int:pk>/", movie_put, name="movie_put")
#   path("detail/<int:pk>/", MovieView.as_view(), name="movie_detail"),
  # path('list/', watch_list, name='watch_list')
  # path('detail/<int:pk>/', movie_detail, name='movie_detail'),
]
