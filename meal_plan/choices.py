# from django.db import models


# class ChoiceModel(models.Model):
#     DISH_STATUS = (
#         ("planning", "Planning"),
#         ("scheduled", "Scheduled"),
#         ("leftover", "Leftover"),
#         ("finished", "Finished"),
#     )

DISH_STATUS = (
    ("planning", "Planning"),
    ("scheduled", "Scheduled"),
    ("leftover", "Leftover"),
    ("finished", "Finished"),
)

MEAL_STATUS = (
    ("planning", "Planning"),
    ("scheduled", "Scheduled"),
    ("leftover", "Leftover"),
    ("finished", "Finished"),
)

GROCERY_STATUS = (
    ("needed", "Needed"),
    ("purchased", "Purchased"),
)

GROCERY_TYPE = (
    ("food", "Food"),
    ("cleaner", "Cleaning Item"),
    ("household", "Household Item"),
)