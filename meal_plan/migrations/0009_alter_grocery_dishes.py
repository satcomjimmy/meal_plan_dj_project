# Generated by Django 5.0.2 on 2024-03-10 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plan', '0008_alter_grocery_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='dishes',
            field=models.ManyToManyField(blank=True, related_name='ingredients', to='meal_plan.dish'),
        ),
    ]