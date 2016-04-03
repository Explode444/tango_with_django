from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title
		

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')