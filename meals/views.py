from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from meals.models import Meal
# Create your views here.
class MealList(ListView):
    model = Meal
    template_name = "meals/meals.html"