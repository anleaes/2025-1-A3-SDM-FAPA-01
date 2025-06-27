from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from .models import Visitor
from rest_framework import viewsets
from .serializers import VisitorSerializer

class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email', 'phone', 'birthdate', 'gender'] # Neste campo coloque somente.