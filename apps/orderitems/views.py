from django.shortcuts import render

from .models import Orderitem
from rest_framework import viewsets
from .serializers import  OrderitemSerializer

class OrderitemViewSet(viewsets.ModelViewSet):
    queryset = Orderitem.objects.all()
    serializer_class = OrderitemSerializer  