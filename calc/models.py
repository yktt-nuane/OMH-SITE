from django.db import models
import os

class PatientPhysical(models.Model):
    age = models.IntegerField(default="")

    sex = models.IntegerField(default="")

    height = models.IntegerField(default="")

    weight = models.IntegerField(default="")

class Nutrition(models.Model):
    energy = models.IntegerField(default="")

    sugar = models.IntegerField(default="")

    protein = models.IntegerField(default="")

    lipid = models.IntegerField(default="")

    water = models.IntegerField(default="")

    salt = models.IntegerField(default="")

    potassium = models.IntegerField(default="")
