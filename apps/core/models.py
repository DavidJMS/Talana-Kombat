from django.db import models


class EspecialMovements(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    damage = models.IntegerField(default=1)


class Fighter(models.Model):
    name = models.CharField(max_length=50, unique=True)
    movements = models.ManyToManyField(EspecialMovements)
    energy = models.IntegerField()
