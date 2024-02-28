from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Reviews(models.Model):
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='reviews_like')

    def number_of_likes(self):
        return self.likes.count()
    
