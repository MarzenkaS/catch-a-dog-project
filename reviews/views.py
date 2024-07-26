from django.shortcuts import render, redirect, get_object_or_404, reverse
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
    comments = review.comments.all().order_by("-created_on")
    comment_count = review.comments.count()  # Count all comments, regardless of approval status

    # Initialize forms
    comment_form = CommentForm()
    review_form = ReviewForm(instance=review)

    if request.method == "POST":
        if 'edit_review' in request.POST:  # Handle review update
            review_form = ReviewForm(data=request.POST, files=request.FILES, instance=review)
            if review_form.is_valid() and review.author == request.user:
                updated_review = review_form.save(commit=False)
                updated_review.approved = False
                updated_review.save()
                messages.success(request, 'Review updated')
                return HttpResponseRedirect(reverse('reviews_detail', args=[pk]))
            else:
                messages.error(request, 'Error updating review!')
        else:  # Handle comment submission
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.reviews = review
                comment.save()
                messages.success(request, 'Comment submitted!')
                return HttpResponseRedirect(reverse('reviews_detail', args=[pk]))

    return render(request, "reviews/reviews_detail.html",
                  {
                   "review": review,
                   "comments": comments,
                   "comment_count": comment_count,
                   "comment_form": comment_form,
                   "review_form": review_form,
                  }
                  )


def comment_edit(request, pk, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        review = get_object_or_404(Reviews, pk=pk)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.reviews = review
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment Updated!')
            return HttpResponseRedirect(reverse('reviews_detail', args=[pk]))
        else:
            messages.error(request, 'Error updating comment!')

    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'comment_edit.html', {'comment_form': comment_form})


def comment_delete(request, pk, comment_id):
    """
    View to delete comment
    """
    review = get_object_or_404(Reviews, pk=pk)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('reviews_detail', args=[pk]))


def add_review(request):
    """
    View to add a new review
    """
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, files=request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request, 'Review has been added')
            return redirect('home')
    else:
        review_form = ReviewForm()

    return render(request, "reviews/add_review.html",
                  {'review_form': review_form})


def review_edit(request, review_id):
    """
    View to edit reviews.
    """
    review = get_object_or_404(Reviews, pk=review_id)

    # Check if the logged-in user is the author of the review
    if review.author != request.user:
        messages.error(request, "You do not have permission to edit this review.")
        return HttpResponseRedirect(reverse('reviews_detail', args=[review_id]))

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid():
            updated_review = review_form.save(commit=False)
            updated_review.approved = False  # Optionally set to False if it requires re-approval
            updated_review.save()
            messages.success(request, 'Review Updated!')
            return HttpResponseRedirect(reverse('reviews_detail', args=[review_id]))
        else:
            messages.error(request, 'Error updating review!')
    else:
        review_form = ReviewForm(instance=review)

    return render(request, 'review_edit.html', {'review_form': review_form})


def review_delete(request, pk, review_id):
    """
    view to delete reviews
    """
    review = get_object_or_404(Reviews, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.success(request, 'Review deleted!')
    else:
        messages.error(request, 'You can only delete your own review!')

    return HttpResponseRedirect(reverse('home'))
