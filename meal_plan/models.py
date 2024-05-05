from datetime import date
from django.db import models
from django.urls import reverse
from .choices import DISH_STATUS, MEAL_STATUS, GROCERY_STATUS, GROCERY_TYPE


class Grocery(models.Model):
    name = models.CharField(max_length=255)
    qty_needed = models.IntegerField(default=1)
    when_needed = models.DateField(default=date.today)
    type = models.CharField(choices=GROCERY_TYPE, default="food", max_length=250)
    status = models.CharField(choices=GROCERY_STATUS, default="needed", max_length=250)
    # dishes = models.ManyToManyField(
    #     Dish,
    #     related_name="ingredients",
    #     blank=True
    #     )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("meal_plan:grocery_detail", args=[self.pk])
    
    class Meta:
        verbose_name_plural = "groceries"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(choices=DISH_STATUS, max_length=250)
    recipe = models.CharField(max_length=255, blank=True)
    ingredients = models.ManyToManyField(
        Grocery,
        # related_name="ingredients",
        blank=True
        )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("meal_plan:dish_detail", args=[self.pk])

    class Meta:
        verbose_name_plural = "dishes"
    

class Meal(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(choices=MEAL_STATUS, max_length=250)
    dishes = models.ManyToManyField(
        Dish,
        related_name="meals",
        blank=True
        )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("meal_plan:meal_detail", args=[self.pk])
    

