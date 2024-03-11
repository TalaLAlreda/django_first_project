from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    product_type = models.CharField(max_length = 20)
    image = models.CharField(max_length = 150)
    quantity = models.IntegerField()
    price = models.FloatField()
    description = models.CharField(max_length = 250)
    weight = models.FloatField()
    color = models.CharField(max_length = 20)
    shipment_fee = models.FloatField()
    manufacturer = models.CharField(max_length = 20)
    warranty = models.IntegerField()

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    payed = models.BooleanField()

class CartProducts(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
