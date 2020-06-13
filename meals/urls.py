from django.urls import path
from meals.views import MealList
urlpatterns = [
    path('', MealList.as_view())
]