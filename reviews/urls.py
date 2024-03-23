from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewsList.as_view(), name='home'),
    path('reviews_detail/<int:pk>/', views.reviews_detail, name='reviews_detail'),
    path('add_review/', views.add_review, name='add_review'),
    path('reviews_detail/<int:pk>/edit_review/<int:review_id>', views.review_edit, name='review_edit'),
    path('reviews_detail/<int:pk>/delete_review/<int:review_id>', views.review_delete, name='review_delete'),
    path('reviews_detail/<int:pk>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('reviews_detail/<int:pk>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]


    





