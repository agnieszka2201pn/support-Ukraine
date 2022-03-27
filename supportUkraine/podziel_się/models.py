from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class CurrentNeeds(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    amount = models.IntegerField()
    date = models.DateField(null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

