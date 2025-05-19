from django.db import models

class People(models.Model):
	firstName = models.CharField(max_length=255)
	lastName = models.CharField(max_length=255)
	email = models.CharField(max_length=255, null=True)
	phone = models.IntegerField(null=True)

