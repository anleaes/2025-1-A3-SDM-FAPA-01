from django.db import models
from artists.models import Artist
from movements.models import Movement

# Create your models here.
class Piece(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    movement = models.ForeignKey(Movement, on_delete=models.SET_NULL, null=True)
    year = models.PositiveIntegerField()
    # image = models.ImageField()
    
    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
        ordering =['id']

    def __str__(self):
        return self.name