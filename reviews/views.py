from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Reviews, Comment

# Create your views here.

class ReviewsList(generic.ListView):
    queryset = Reviews.objects.all()
    template_name = "reviews/index.html"
    paginate_by = 4


def reviews_detail(request, pk):
    """
    Display an individual review

    """
    review = get_object_or_404(Reviews, id=pk)
    comments = review.comments.all().order_by("-created_on")
    comment_count = review.comments.filter(approved=True).count()
    review_likes = review.likes.count()

    return render(request, "reviews/reviews_detail.html",
        {
            "review": review,
            "comments": comments,
            "comment_count": comment_count,
            "review_likes": review_likes,
        }
    )
 
