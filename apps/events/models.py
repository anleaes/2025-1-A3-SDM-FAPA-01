from django.db import models
from pieces.models import Piece
from museums.models import Museum
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    pieces = models.ManyToManyField(Piece)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering =['id']

    def __str__(self):
        return self.name