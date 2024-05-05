"""
URL configuration for HomePage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'meal_plan'
urlpatterns = [
    # path('', views.DishFormView.as_view(), name='dish_form'),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('dishes/', views.DishListView.as_view(), name='dish_list'),
    path('entry_success', views.FormSuccessView.as_view(), name='form_success'),
    path('delete_success', views.DeleteSuccessView.as_view(), name='delete_success'),
    path('dish_create/', views.DishCreateView.as_view(), name='dish_create'),
    path('dish_detail/<int:pk>', views.DishDetailView.as_view(), name='dish_detail'),
    path('dish_update/<int:pk>', views.DishUpdateView.as_view(), name='dish_update'),
    path('dish_delete/<int:pk>', views.DishDeleteView.as_view(), name='dish_delete'),
    path('meals/', views.MealListView.as_view(), name='meal_list'),
    path('meal_create/', views.MealCreateView.as_view(), name='meal_create'),
    path('meal_detail/<int:pk>', views.MealDetailView.as_view(), name='meal_detail'),
    path('meal_update/<int:pk>', views.MealUpdateView.as_view(), name='meal_update'),
    path('meal_delete/<int:pk>', views.MealDeleteView.as_view(), name='meal_delete'),
    path('grocery_list/', views.GroceryListView.as_view(), name='grocery_list'),
    path('grocery_create/', views.GroceryCreateView.as_view(), name='grocery_create'),
    path('grocery_detail/<int:pk>', views.GroceryDetailView.as_view(), name='grocery_detail'),
    path('grocery_update/<int:pk>', views.GroceryUpdateView.as_view(), name='grocery_update'),
    path('grocery_delete/<int:pk>', views.GroceryDeleteView.as_view(), name='grocery_delete'),

]
