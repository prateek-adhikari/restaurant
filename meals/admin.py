from django.contrib import admin
from meals.models import Meal, Category
from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class MealAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

# Register your models here.
admin.site.register(Meal, MealAdmin) 
admin.site.register(Category)