from django.urls import path 
from .views import MoviesList , MoviesDetail

urlpatterns = [
    path('movies/', MoviesList.as_view(), name='movies_list'),
    path('movies/<int:pk>/', MoviesDetail.as_view(), name='movies_detail'),
]