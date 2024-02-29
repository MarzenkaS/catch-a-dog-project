from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Reviews(models.Model):
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='reviews_like')

    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Posted by {self.author}"



class Comment(models.Model):
    reviews = models.ForeignKey(
        Reviews, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.body} Comment by {self.author}"         
    
