from django.db import models

class Greetings(models.Model):
	firstgreet = models.CharField(max_length=255)
	secondgreet = models.CharField(max_length=255)
	language = models.CharField(max_length=255, null=True)
	count = models.IntegerField(null=True)

