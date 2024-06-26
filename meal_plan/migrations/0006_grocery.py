# Generated by Django 5.0.2 on 2024-03-10 02:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plan', '0005_alter_meal_dishes_alter_meal_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('qty_needed', models.IntegerField(default=1)),
                ('when_needed', models.DateField(default=datetime.date.today)),
                ('type', models.CharField(choices=[('food', 'Food'), ('cleaner', 'Cleaning Item'), ('household', 'Household Item')], max_length=250)),
                ('status', models.CharField(choices=[('needed', 'Needed'), ('purchased', 'Purchased')], max_length=250)),
                ('dishes', models.ManyToManyField(blank=True, related_name='ingredient', to='meal_plan.dish')),
            ],
        ),
    ]
