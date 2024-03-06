from django.shortcuts import render
from django.views import generic
from .models import Reviews, Comment

# Create your views here.

class ReviewsList(generic.ListView):
    queryset = Reviews.objects.all()
    template_name = "reviews/index.html"
    paginate_by = 6


class CommentList(generic.ListView):
    queryset = Comment.objects.all()    
