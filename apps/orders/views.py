from django.shortcuts import render

# Create your views here.
from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  