from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()

class Transaction(models.Model):
    type = models.CharField(max_length=10)
    amount = models.FloatField()
    date = models.DateField()

class Sale(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    date = models.DateField()