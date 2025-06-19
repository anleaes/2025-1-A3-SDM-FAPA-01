from django.shortcuts import render

# Create your views here.
from .models import Piece
from rest_framework import viewsets
from .serializers import PieceSerializer

class PieceViewSet(viewsets.ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer  