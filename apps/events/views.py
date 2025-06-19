from django.shortcuts import render

# Create your views here.
from .models import Event
from rest_framework import viewsets
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer  