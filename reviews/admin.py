from django.contrib import admin
from .models import Reviews, Comment, Like
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reviews)
class ReviewsAdmin(SummernoteModelAdmin):

    search_fields = ['date', 'author', 'content',]
    summernote_fields = ('content',)
    list_display = ('author', 'status', 'created_on', )
    list_filter = ('status', 'created_on',)
    

admin.site.register(Like)
admin.site.register(Comment)
