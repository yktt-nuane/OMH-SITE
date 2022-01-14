from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.aggregates import Count
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

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

class Article(models.Model):
    title = models.CharField(default='', max_length=30)
    text = RichTextField(blank=True, null=True)
    author = models.CharField(default='', max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    count = models.IntegerField(default=0,)
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ManyToManyField(Category, blank=True)



class PostArticle(models.Model):
    title = models.CharField(default='', max_length=30)
    text = RichTextUploadingField(blank=True, null=True)
    author = models.CharField(default='', max_length=30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    count = models.IntegerField(default=0,)
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(default='', blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def save(self):
        self.slug = slugify(self.title)
        super(PostArticle, self).save()

    def __str__(self):
        return '%s' % self.title

class Comment(models.Model):
    comment = models.TextField(default="", max_length=500)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey(PostArticle, on_delete=models.CASCADE)
