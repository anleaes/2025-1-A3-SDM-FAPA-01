from django.db import models

# Create your models here.
from pieces.models import Piece
from orders.models import Order

class Orderitem(models.Model):
    quantity = models.PositiveIntegerField('Quantidade',null=True, blank=True,default=0)
    unitary_price = models.DecimalField('Preco unitario', max_digits=10, decimal_places=2)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('order', 'piece')
        verbose_name = 'Item de pedido'
        verbose_name_plural = 'Itens de pedido'
        ordering =['id']

    def __str__(self):
        return f"{self.quantity} - {self.piece.name}"