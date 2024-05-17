""" Models for meal_plan app in home_page project """

from datetime import date
from django.db import models
from django.urls import reverse
from .choices import DISH_STATUS, MEAL_STATUS, GROCERY_STATUS, GROCERY_TYPE


class Grocery(models.Model):
    """
    Defines Grocery items

    Types can be Food, Household or Cleaning supplies

    """
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
        """ Returns a string of the Grocery object name """
        return str(self.name)

    def get_absolute_url(self):
        """ 
        Returns an absolute reverse URL for the detailed view of the Grocery object
        """
        return reverse("meal_plan:grocery_detail", args=[self.pk])

    class Meta:
        """ Metadata about the Grocery objects """
        verbose_name_plural = "groceries"


class Dish(models.Model):
    """
    Defines Dish items

    Dishes can have recipies and child Grocery ingredients

    """
    name = models.CharField(max_length=255)
    status = models.CharField(choices=DISH_STATUS, max_length=250)
    recipe = models.CharField(max_length=255, blank=True)
    ingredients = models.ManyToManyField(
        Grocery,
        # related_name="ingredients",
        blank=True
        )

    def __str__(self):
        """ Returns a string of the Dish object name """
        return str(self.name)

    def get_absolute_url(self):
        """ 
        Returns an absolute reverse URL for the detailed view of the Dish object
        """
        return reverse("meal_plan:dish_detail", args=[self.pk])

    class Meta:
        """ Metadata about the Dish objects """
        verbose_name_plural = "dishes"


class Meal(models.Model):
    """
    Defines Meal items

    Meals can be scheduled, and have child Dishes

    """
    name = models.CharField(max_length=255)
    status = models.CharField(choices=MEAL_STATUS, max_length=250)
    dishes = models.ManyToManyField(
        Dish,
        related_name="meals",
        blank=True
        )

    def __str__(self):
        """ Returns a string of the Meal object name """
        return str(self.name)

    def get_absolute_url(self):
        """ 
        Returns an absolute reverse URL for the detailed view of the Meal object
        """
        return reverse("meal_plan:meal_detail", args=[self.pk])
