from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


class Reviews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, default=None, blank=True, related_name='likes')
    status = models.IntegerField(choices=STATUS, default=0) 

    def __str__(self):
        return f"Posted by {self.author}"
    
    @property
    def num_likes(self):
        return self.likes.all().count()    

    class Meta:
        ordering = ["-created_on"]

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like')

    def __str__(self):
        return str(self.review)



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
    
