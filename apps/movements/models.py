from django.db import models

# Create your models here.
class Movement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    yearFoundation = models.IntegerField(default=1)
    
    class Meta:
        verbose_name = 'Movimento'
        verbose_name_plural = 'Movimentos'
        ordering =['id']
    
    def __str__(self):
        return self.name