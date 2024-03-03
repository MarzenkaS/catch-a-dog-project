from django.contrib import admin
from .models import Reviews, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reviews)
class ReviewsAdmin(SummernoteModelAdmin):

    search_fields = ['date', 'author']
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
