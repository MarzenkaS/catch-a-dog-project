from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Reviews, Comment
from .forms import CommentForm

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
    review_likes = review.likes.count()
    comment_count = review.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.reviews = review
            comment.save()

    comment_form = CommentForm()

    return render(request, "reviews/reviews_detail.html",
        {
            "review": review,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "review_likes": review_likes,
        }
    )
 
