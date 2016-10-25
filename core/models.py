from django.db import models

# Create your models here.


class Product(models.Model):
    code = models.IntegerField()
    product = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Produto'
        verbose_name = 'Produtos'

    def __str__(self):
        return self.product
