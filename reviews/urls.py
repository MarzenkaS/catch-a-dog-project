from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewsList.as_view(), name='home'),
    path('reviews_detail', views.reviews_detail, name='reviews_detail'),
]