from django import forms
# from home_page.widget import DatePickerInput
from .models import Dish, Meal, Grocery


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            'name',
            'status',
            'recipe',
            'ingredients',
        ]


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = [
            'name',
            'status',
            'dishes',
        ]


class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = [
            'name',
            'qty_needed',
            'when_needed',
            'type',
            'status',
            # 'dishes',
        ]
        # widgets = {
        #     'when_needed' : DatePickerInput(),
        # }