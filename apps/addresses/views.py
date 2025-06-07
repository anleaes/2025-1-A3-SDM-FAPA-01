from django.shortcuts import render

# Create your views here.

from .models import Address
from rest_framework import viewsets
from .serializers import AddressSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer  