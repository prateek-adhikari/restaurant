from django.urls import path
from meals.views import MealList, MealDetail
urlpatterns = [
    path('', MealList, name="meallist"),
    path('<slug>', MealDetail.as_view(), name="mealdetail"),
]