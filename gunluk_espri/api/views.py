from rest_framework import generics
from app.models import Tweet
from .serializers import TweetSerializer

class TweetListAPIView(generics.ListAPIView):
    queryset = Tweet.objects.filter(active=True).order_by('-order', '-create_date')
    serializer_class = TweetSerializer

class TweetDetailAPIView(generics.RetrieveAPIView):
    queryset = Tweet.objects.filter(active=True)
    serializer_class = TweetSerializer
