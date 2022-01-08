from django.db import models
import os

class PatientPhysical(models.Model):
    age = models.IntegerField(default="")

    sex = models.IntegerField(default="")

    height = models.IntegerField(default="")

    weight = models.IntegerField(default="")
