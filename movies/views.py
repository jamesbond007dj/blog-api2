from django.shortcuts import render
from rest_framework import generics
from .models import Movies
from .serializers import MoviesSerializer
from .permissions import IsAuthorOrReadOnly

class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MoviesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (IsAuthorOrReadOnly,)