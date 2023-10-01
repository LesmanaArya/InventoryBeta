from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Item(models.Model):  # Data Model for Class Item
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    description = models.TextField(default='')
    effect = models.TextField(default='')
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name