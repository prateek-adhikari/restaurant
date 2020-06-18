from django.shortcuts import render
from meals.models import Meal, Category
from blog.models import Post
from aboutus.models import whyChooseUs
# Create your views here.
def home(request):
    meals = Meal.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.filter().order_by('-created')[:3]
    lastpost = Post.objects.filter().order_by('-created')[0]
    whychooseus = whyChooseUs.objects.all() 
    context = {
        "meals": meals,
        "posts": posts,
        "lastpost": lastpost,
        "whychoose": whychooseus,
        "categories": categories
    }
    return render(request, 'home/home.html', context)