from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    tags = TaggableManager(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content