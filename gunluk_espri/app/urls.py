from django.urls import path
from . import views

urlpatterns = [
    path("", views.timeline, name="timeline"),
    path("profile/<int:id>/", views.profile, name="profile"),
]