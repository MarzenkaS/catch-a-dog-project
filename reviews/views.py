from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Reviews, Comment

# Create your views here.

class ReviewsList(generic.ListView):
    queryset = Reviews.objects.all()
    template_name = "reviews/index.html"
    paginate_by = 4


def reviews_detail(request):
    """
    Display an individual review

    """

    queryset = Reviews.objects.filter(status=1)
    reviews = get_object_or_404(queryset)
    comments = reviews.comments.all().order_by("-created_on")
    comment_count = reviews.comments.filter(approved=True).count()
    reviews_likes.count = reviews.filter(approved=True).likes.count()


    return render(request, "reviews/reviews_detail.html",
        {"reviews": reviews
        "comments": comments,
        "comment_count": comment_count,
        "reviews_likes.count": reviews_likes.count,
        },
    )
 
