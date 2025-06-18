from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Museum


class MuseumViewSet(viewsets.ModelViewSet):
    queryset = Museum.objects.all()
    
