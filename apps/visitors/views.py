from django.shortcuts import render

# Create your views here.
from .models import Visitor
from rest_framework import viewsets
from .serializers import VisitorSerializer

class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer