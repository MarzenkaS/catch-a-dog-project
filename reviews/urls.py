from . import views
from django.urls import path
from .views import like_reviews

urlpatterns = [
    path('', views.ReviewsList.as_view(), name='home'),
    path('reviews_detail/<int:pk>/', views.reviews_detail, name='reviews_detail'),
    path('reviews_detail/like_reviews/<int:reviews_id>', like_reviews, name='like_reviews'),
    path('reviews_detail/<int:pk>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('reviews_detail/<int:pk>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]





