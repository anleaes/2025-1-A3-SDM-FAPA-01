from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering =['id']

    def __str__(self):
        return f"{self.street}, {self.number} - {self.city}, {self.country}"