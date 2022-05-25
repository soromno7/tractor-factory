from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.



class IsVoited(models.Model):
    user = models.CharField(max_length = 100)
    is_voted = models.BooleanField()


class Part(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField(max_length=100)

class Vote(models.Model):
    partA = models.ForeignKey(Part, related_name='partA', on_delete = models.PROTECT)
    partB = models.ForeignKey(Part, related_name='partB', on_delete = models.PROTECT)
    partC = models.ForeignKey(Part, related_name='partC', on_delete = models.PROTECT)

class Kondorse(models.Model):
    place1 = models.CharField(max_length = 50)
    place2 = models.CharField(max_length = 50)
    place3 = models.CharField(max_length = 50)

    



