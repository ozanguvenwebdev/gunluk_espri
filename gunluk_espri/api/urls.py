from django.urls import path
from .views import TweetListAPIView, TweetDetailAPIView

urlpatterns = [
    path('tweets/', TweetListAPIView.as_view(), name='api-tweet-list'),
    path('tweets/<int:pk>/', TweetDetailAPIView.as_view(), name='api-tweet-detail'),
]
