from django.urls import path
from watchlist_app.api.views import *

urlpatterns = [
    path('list/', watch_list, name='watch_list')
    # path('detail/<int:pk>/', movie_detail, name='movie_detail'),
]
