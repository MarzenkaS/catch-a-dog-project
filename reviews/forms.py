from .models import Comment, Reviews
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('content',)
