from django.contrib import admin
from aboutus.models import aboutUs,whyChooseUs,chef
# Register your models here.

admin.site.register([
    aboutUs,
    whyChooseUs,
    chef
])