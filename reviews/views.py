from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Reviews, Comment, Like
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
    author = request.user
    comments = review.comments.all().order_by("-created_on")
    comment_count = review.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.reviews = review
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(request, "reviews/reviews_detail.html",
        {
            "review": review,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


def like_reviews(request, reviews_id):
    user = request.user
    if request.Method == 'POST':
        reviews_id = request.POST.get('reviews_id')
        reviews.obj = Reviews.objects.get(id=reviews_id)

        if user in reviews.obj.likes.all():
            reviews_obj.likes.remove(user)
        else:
            reviews.obj.likes.add(user)

        like = Like.objects.get(user=user, reviews_id=reviews_id)

        like.save()                  
            
    return self.likes.all().count()

 

def comment_edit(request, pk, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Reviews.objects.filter(status=1)
        review = get_object_or_404(queryset, pk=pk)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)                       

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.reviews = review
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('reviews_detail', args=[pk]))


def comment_delete(request, pk, comment_id):
    """
    view to delete comment
    """
    queryset = Reviews.objects.filter(status=1)
    review = get_object_or_404(queryset, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('reviews_detail', args=[pk]))


def AddReview(request):   
    """
    view to add new review
    """ 


def review_edit(request, event_id, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=event_id)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)  

        if review_form.is_valid() and review.reviewer == request.user:
            review = review_form.save(commit=False)
            review.reviewer = request.user
            review.event = event
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Review!')

    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))


def review_delete(request, event_id, review_id):
    """
    view to delete reviews
    """
    if request.method == "POST":        