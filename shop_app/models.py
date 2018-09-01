from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    category = models.ForeignKey('Category', on_delete='CASCADE', null=True, related_name='products')

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return  self.title

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete='CASCADE')
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)