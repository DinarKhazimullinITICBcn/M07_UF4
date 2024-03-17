from django.db import models

# Create your models here.
class Persona(models.Model):
    nom = models.CharField(max_length=200)
    cognom = models.CharField(max_length=200)
    edat = models.IntegerField()
    correu = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    moduls = models.CharField(max_length=200)
