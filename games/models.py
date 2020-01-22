from django.db import models
from django.contrib.auth.models import User

class Games(models.Model):
    user_main = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title