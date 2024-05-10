from django.db import models
from django.urls import reverse

class Company(models.Model):
    name=models.CharField(max_length=20)
    Ceo=models.CharField(max_length=20)
    Location=models.CharField(max_length=25)

    def get_absolute_url(self):
        return reverse('create',kwargs={'pk':self.pk})
