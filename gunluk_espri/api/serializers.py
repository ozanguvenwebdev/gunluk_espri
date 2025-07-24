from rest_framework import serializers
from app.models import Tweet, Profile  # main yerine gerçek app adın neyse onu yaz

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'display_name', 'description', 'email']

class TweetSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'profile', 'content', 'create_date', 'order']
