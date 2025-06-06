from django.shortcuts import render

# Create your views here.

from .models import Artist
from rest_framework import viewsets
from .serializers import ArtistSerializer

