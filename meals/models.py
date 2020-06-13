from django.db import models
from django.utils.text import slugify
# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meal, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.name,self.price)