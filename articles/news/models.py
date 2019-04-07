from django.db import models
from django import forms



# Create your models here.




class Article(models.Model):
	title = models.CharField(max_length=200, default=None)
	text = models.CharField(max_length=2000)
	comments_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	author = models.CharField(max_length=200)

	def __str__(self):
		return self.title

# this displays the object more explicitly with some kind of data from iside the object shown on the outside




class Comment(models.Model):
	text = models.CharField(max_length=200)
	user = models.CharField(max_length=200)

	
	def __str__(self):
		return self.text











# class Author(models.Model):
#     articles = models.CharField(max_length=200)
