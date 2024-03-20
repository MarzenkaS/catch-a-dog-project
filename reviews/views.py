from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Reviews, Comment
from .forms import CommentForm, ReviewForm



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


def add_review(request):
    """
    View to add a new review
    """
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request, 'Review submitted and awaiting approval')
            return redirect('review_detail', pk=review.pk)  # Redirect to review detail page or any other appropriate page
    else:
        review_form = ReviewForm()
   
    return render(request, "reviews/add_review.html", {'review_form': review_form})


def review_edit(request, event, review):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Event.objects.all()
        event = get_object_or_404(queryset, event)
        review = get_object_or_404(Review, review)
        review_form = ReviewForm(data=request.POST, instance=review)  

        if review_form.is_valid() and review.reviewer == request.user:
            review = review_form.save(commit=False)
            review.event = event
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Review!')

    return HttpResponseRedirect(reverse('event_detail', args=[event]))


def review_delete(request, event, review):
    """
    view to delete reviews
    """
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, event)
    review = get_object_or_404(Review, review)
    review_form = ReviewForm(data=request.POST, instance=review) 

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own review!')

    return HttpResponseRedirect(reverse('event_detail', args=[event]))      