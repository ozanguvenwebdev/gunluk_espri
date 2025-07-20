from django.shortcuts import render, redirect
from app.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html", {})