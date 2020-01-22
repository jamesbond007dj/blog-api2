from django.shortcuts import render
from rest_framework import generics
from .models import Games
from .serializers import GamesSerializer 
from .permissions import IsAuthorOrReadOnly

class GamesList(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer

class GamesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = (IsAuthorOrReadOnly,)