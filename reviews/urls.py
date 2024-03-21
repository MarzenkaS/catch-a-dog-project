from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewsList.as_view(), name='home'),
    path('reviews_detail/<int:pk>/', views.reviews_detail, name='reviews_detail'),
    path('add_review/', views.add_review, name='add_review'),
    path('add_review/', views.review_edit, name='review_edit'),
    path('add_review/', views.review_delete, name='review_delete'),
    path('reviews_detail/<int:pk>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('reviews_detail/<int:pk>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]


    path('edit_review/<int:event_id>/<int:review_id>/', views.review_edit, name='review_edit'),
    path('delete_review/<int:event_id>/<int:review_id>/', views.review_delete, name='review_delete'),





