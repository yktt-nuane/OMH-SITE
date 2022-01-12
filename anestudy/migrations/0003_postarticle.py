# Generated by Django 4.0.1 on 2022-01-12 04:20

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anestudy', '0002_alter_article_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('author', models.CharField(default='', max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, default='')),
                ('tags', models.ManyToManyField(blank=True, to='anestudy.Tag')),
            ],
        ),
    ]
