# Generated by Django 4.2.11 on 2024-03-11 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeAppliance', '0002_cart_cartproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='payed',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
