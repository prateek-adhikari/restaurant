from django.db import models

# Create your models here.
class aboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="aboutus/")
    def __str__(self):
        return self.title

class whyChooseUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return self.title

class chef(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to="chef/")
    def __str__(self):
        return self.name