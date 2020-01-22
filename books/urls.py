from django.urls import path 
from .views import BooksList , BooksDetail

urlpatterns = [
    path('books/', BooksList.as_view(), name='books_list'),
    path('books/<int:pk>/', BooksDetail.as_view(), name='books_detail'),
]