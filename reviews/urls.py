from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewsList.as_view(), name='home'),
    path('reviews_detail/<int:pk>/', views.reviews_detail, name='reviews_detail'),
    path('comments/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
]
