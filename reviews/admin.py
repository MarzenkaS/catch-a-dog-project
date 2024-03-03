from django.contrib import admin
from .models import Reviews, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reviews)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('status')
    search_fields = ['date', 'user_name']
    list_filter = ('status',)
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)
