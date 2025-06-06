from django.shortcuts import render

# Create your views here.

from .models import Movement
from rest_framework import viewsets
from .serializer import MovementSerializer

class MovementViewSet(viewsets.ModelViewSet):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer  