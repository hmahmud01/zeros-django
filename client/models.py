from django.db import models
from datetime import date

from django.contrib.auth.models import User

# Create your models here.
class FoodItems(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    qty = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Images(models.Model):
    food = models.ForeignKey(FoodItems, related_name='this_food', on_delete=models.CASCADE)
    images = models.FileField('app_files', upload_to='foods/images', blank=True, null=True)

    def __str__(self):
        return self.food

class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, blank=False)
    name = models.CharField(max_length=64, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.phone
    