from typing import Any
from django.utils import timezone
from django.shortcuts import render #, render_to_response
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views import View
from .forms import DishForm, MealForm, GroceryForm
from .models import Dish, Meal, Grocery
   
def index(request):
    """The home page for the Meal Plan app."""
    return render(request, 'meal_plan/index.html') 


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Item has been saved successfully.")
    

class DeleteSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("You have successfully deleted this item.")
    
# Dish views
class DishFormView(LoginRequiredMixin, FormView):
    template_name = 'meal_plan/dish_form.html'
    form_class = DishForm
    # success_url = '/meal_plan/entry_success'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
   

class DishListView(ListView):
    model = Dish
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    

class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    fields = ['name', 'status', 'recipe', 'ingredients']
    template_name = 'meal_plan/dish_form.html'
    # success_url = '/meal_plan/entry_success'
        

class DishDetailView(DetailView):
    model = Dish
    template_name = 'meal_plan/dish_detail.html'


class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dish
    fields = ['name', 'status', 'recipe', 'ingredients']
    template_name = 'meal_plan/dish_form.html'
    # success_url = '/meal_plan/entry_success'


class DishDeleteView(LoginRequiredMixin, DeleteView):
    model = Dish
    template_name = 'meal_plan/dish_delete_form.html'
    success_url = '/meal_plan/delete_success'

# Meal views
class MealFormView(LoginRequiredMixin, FormView):
    template_name = 'meal_plan/meal_form.html'
    form_class = MealForm
    # success_url = '/meal_plan/entry_success'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
   

class MealListView(ListView):
    model = Meal
    # paginate_by = 10

    # def detail(request, dish_id):
    #     dish = Dish.objects.get(pk=dish_id)
    #     meals = dish.meal.all()

    #     return render_to_response('meal_list/html',)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['name', 'status', 'dishes']
    template_name = 'meal_plan/meal_form.html'
    # success_url = '/meal_plan/entry_success'
        

class MealDetailView(DetailView):
    model = Meal
    template_name = 'meal_plan/meal_detail.html'


class MealUpdateView(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = ['name', 'status', 'dishes']
    template_name = 'meal_plan/meal_form.html'
    # success_url = '/meal_plan/entry_success'


class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = Meal
    template_name = 'meal_plan/meal_delete_form.html'
    success_url = '/meal_plan/delete_success'


# Grocery views
class GroceryFormView(LoginRequiredMixin, FormView):
    template_name = 'meal_plan/grocery_form.html'
    form_class = GroceryForm
    # success_url = '/meal_plan/entry_success'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
   

class GroceryListView(ListView):
    model = Grocery
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    

class GroceryCreateView(LoginRequiredMixin, CreateView):
    model = Grocery
    fields = [
            'name',
            'qty_needed',
            'when_needed',
            'type',
            'status',
            # 'dishes',
        ]
    template_name = 'meal_plan/grocery_form.html'
    # success_url = '/meal_plan/entry_success'
        

class GroceryDetailView(DetailView):
    model = Grocery
    template_name = 'meal_plan/grocery_detail.html'


class GroceryUpdateView(LoginRequiredMixin, UpdateView):
    model = Grocery
    fields = [
            'name',
            'qty_needed',
            'when_needed',
            'type',
            'status',
            # 'dishes',
        ]
    template_name = 'meal_plan/grocery_form.html'
    # success_url = '/meal_plan/entry_success'


class GroceryDeleteView(LoginRequiredMixin, DeleteView):
    model = Grocery
    template_name = 'meal_plan/grocery_delete_form.html'
    success_url = '/meal_plan/delete_success'