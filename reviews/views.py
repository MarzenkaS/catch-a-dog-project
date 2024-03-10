from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Reviews, Comment

# Create your views here.

class ReviewsList(generic.ListView):
    queryset = Reviews.objects.all()
    template_name = "reviews/index.html"
    paginate_by = 4


def reviews_detail(request, slug):
    """
    Display an individual review

    """

    queryset = Reviews.objects.filter(status=1)
    reviews = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "reviews/reviews_detail.html",
        {"reviews": reviews},
    )



class CommentList(generic.ListView):
    queryset = Comment.objects.all()    
