from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Product(models.Model):
    code = models.IntegerField()
    product = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Produto'
        verbose_name = 'Produtos'

    def __str__(self):
        return self.product

    def get_absolute_url(self):
        return reverse('core:product_detail', kwargs={"pk": self.pk})
