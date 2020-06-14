from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
)
from meals.models import Meal,Category
# Create your views here.
def MealList(request):
    meal = Meal.objects.all()
    category = Category.objects.all()
    context = {
        "meal_list": meal,
        "category_list": category
    }   
    return render(request, "meals/meals.html", context)

class MealDetail(DetailView):
    model = Meal
    template_name = "meals/mealsdetail.html"