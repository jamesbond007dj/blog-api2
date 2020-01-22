from django.urls import path 
from .views import GamesList , GamesDetail

urlpatterns = [
    path('games/', GamesList.as_view(), name='games_list'),
    path('games/<int:pk>/', GamesDetail.as_view(), name='games_detail'),
]