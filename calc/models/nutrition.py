from django.db import models
import os
from django.utils.crypto import get_random_string

def create_id():
    return get_random_string(22)

def upload_image_to(instance, filename):
    item_id = str(instance.id)
    return os.path.join('static', 'items', item_id, filename)

class Tag(models.Model):
    slug = models.CharField(primary_key=True, unique=True, max_length=20)

    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.slug

class Category(models.Model):
    slug = models.CharField(primary_key=True, unique=True, max_length=20)

    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.slug


class Nutrition(models.Model):
    id = models.CharField(default=create_id, primary_key=True, max_length=20, editable=False)

    name = models.CharField(default='', max_length=20)

    energy = models.IntegerField(default="")

    sugar = models.IntegerField(default="")

    protein = models.IntegerField(default="")

    lipid = models.IntegerField(default="")

    water = models.IntegerField(default="")

    salt = models.IntegerField(default="")

    potassium = models.IntegerField(default="")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    tags = models.ManyToManyField(Tag, blank=True)

    image = models.ImageField(default="", blank=True, upload_to=upload_image_to)

    def __str__(self):
        return self.name
