from django.db import models
from addresses.models import Address

class Museum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dateFoundation = models.DateField()
    contact = models.EmailField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Museu'
        verbose_name_plural = 'Museus'
        ordering =['id']

    def __str__(self):
        return self.name
