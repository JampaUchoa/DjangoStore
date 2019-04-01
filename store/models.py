from django.db import models
from datetime import datetime

class Client(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    # It should be hashed
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=5,default=0)
    def __str__(self):
        return self.name

class Order(models.Model):
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    products = models.ManyToManyField(Product)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.status + " - " + self.created_at.strftime("%m/%d/%Y, %H:%M:%S")
