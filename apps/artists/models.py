from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    
    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering =['id']

    def __str__(self):
        return self.name