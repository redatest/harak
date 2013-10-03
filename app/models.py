# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
#from ckeditor.fields import HTMLField



class New(models.Model):
	title 			= models.CharField(max_length=50, default = 'عنوان')
	published		= models.DateField(help_text='Format daty: 2009-04-28')
	image 			= models.ImageField(upload_to='news')
	html_body 		= models.TextField(blank=True, verbose_name='HTML version')
	
	
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return '/news/%s' %self.id
		
class WatchNew(models.Model):
	title 			= models.CharField(max_length=50, default = 'عنوان')
	published		= models.DateField(help_text='Format daty: 2009-04-28')
	image 			= models.ImageField(upload_to='news')
	html_body 		= models.TextField(blank=True, verbose_name='HTML version')
	
	
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return '/watchnews/%s' %self.id
		

class Statement(models.Model):
	title 			= models.CharField(max_length=50, default = 'البيان')
	published		= models.DateField(help_text='Format daty: 2009-04-28')
	image 			= models.ImageField(upload_to='news')
	html_body 		= models.TextField(blank=True, verbose_name='HTML version')
	
	
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return '/statement/%s' %self.id

class Album(models.Model):
	title 			= models.CharField(max_length=50, default = 'album')
	description		= models.CharField(max_length=50, default = 'description')
	

	def __unicode__(self):
		return self.title
				
class Img(models.Model):
	image 			= models.ImageField(upload_to='news')
	published		= models.DateField(help_text='Format daty: 2009-04-28')
	photos  		= models.ForeignKey(Album)
	
	
	


