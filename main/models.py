from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    description = models.TextField(default='')
    effect = models.TextField(default='')
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name
