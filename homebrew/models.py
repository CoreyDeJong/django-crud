from django.db import models
from django.urls import reverse

# Create your models here.

class Beers(models.Model):
    brewery = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    abv = models.CharField(max_length=64)
    ibu = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('beer_detail', args=[str(self.id)])