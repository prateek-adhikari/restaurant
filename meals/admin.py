from django.contrib import admin
from meals.models import Meal, Category
# Register your models here.
admin.site.register([
    Meal,
    Category,
])