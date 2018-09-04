# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.


class Category(models.Model):
    label = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
# permet de changer le nom de category une fois passé au pluriel
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
# permet d affichier les noms des categories dans la creation d un article
    def __unicode__(self):
        return self.label

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    short_description = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True, 
                                verbose_name="Date de creation")
    date_parution = models.DateTimeField(null=True, blank=True,
                                verbose_name="Date de parution")
    date_update = models.DateTimeField(auto_now=True, 
                                verbose_name="Date de mise a jour")
    cover = models.ImageField( upload_to="article", null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    

class Comment(models.Model):
    fullname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    email = models. EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution ")
    article = models.ForeignKey(Article, null=True, blank=True)
    parent = models.ForeignKey('self',  null=True, blank=True)


