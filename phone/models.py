from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 50)

class ItemDetails(models.Model):
    color = models.CharField(max_length = 50)
    price = models.FloatField()
    quantity = models.IntegerField()
    tax = models.FloatField()
    total = models.FloatField()
    image = models.CharField(max_length = 150)
    date = models.DateTimeField(auto_now_add = True)
    itemId = models.ForeignKey(Item, on_delete = models.CASCADE)
    
class Cart(models.Model):
    id_product = models.IntegerField()
    id_user = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    tax = models.FloatField()
    total = models.FloatField()
    discount = models.FloatField()
    net = models.FloatField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add = True)