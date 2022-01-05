from django.db import models
import os

class Nutrition(models.Model):
    energy = models.IntegerField(default="")

    protein = models.IntegerField(default="")

    lipid = models.IntegerField(default="")

"""
    炭水化物 = models.IntegerField(default="")

    水分 = models.IntegerField(default="")

    塩分 = models.IntegerField(default="")

    総量 = models.IntegerField(default="")

"""
