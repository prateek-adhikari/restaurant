from django.shortcuts import render
from aboutus.models import aboutUs,whyChooseUs,chef
# Create your views here.
def about(request):
    about = aboutUs.objects.all()
    whychoose = whyChooseUs.objects.all()
    chefs = chef.objects.all()
    context = {
        "about": about,
        "whychoose": whychoose,
        "chefs": chefs
    }
    return render(request, 'aboutus/about.html', context)