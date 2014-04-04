from django.db import models

class URLS(models.Model):
	url = models.CharField(max_length=200)
	def __str__(self):
		return self.url
	
class TAGS(models.Model):
	tag = models.CharField(max_length=200)
	url= models.ManyToManyField(URLS)
	def __str__(self):
		return self.tag
