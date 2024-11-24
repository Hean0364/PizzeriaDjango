# Generated by Django 5.1.3 on 2024-11-23 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RestauranteData', '0003_fooditem_restaurante_food_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoFoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestauranteData.fooditem')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pedidos.pedido')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='food_items',
            field=models.ManyToManyField(through='Pedidos.PedidoFoodItem', to='RestauranteData.fooditem'),
        ),
    ]
