from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'id' , 'user_main', 'title', 'author', 'created_at'
        ]