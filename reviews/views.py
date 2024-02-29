from django.shortcuts import render
from django.views import generic
from .models import Reviews, Comment

# Create your views here.

class ReviewsList(generic.ListView):
    model = Reviews
