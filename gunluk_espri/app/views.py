from django.shortcuts import render, redirect
from app.models import *
from django.contrib import messages
from django.core.paginator import Paginator
from .models import *

def timeline(request):
    page = request.GET.get("page", 1)

    tweets = Tweet.objects.filter(active=True)
    tweets = sorted(tweets, key=lambda t: t.score, reverse=True)

    paginator = Paginator(tweets, 10)
    page_obj = paginator.get_page(page)

    if request.htmx:
        return render(request, "partials/tweet_list.html", {"tweets": page_obj})

    return render(request, "index.html", {"tweets": page_obj})


def profile(request, id):
    
    profile = Profile.objects.get(id=id)
    tweets = Tweet.objects.filter(active=True).order_by('-order', '-create_date')

    paginator = Paginator(tweets, 10)
    page_obj = paginator.get_page(page)

    if request.htmx:
        return render(request, "partials/tweet_list.html", {"tweets": page_obj})

    return render(request, "index.html", {"tweets": page_obj})