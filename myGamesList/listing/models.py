from django.db import models

class Games(models.Model):
	name = models.CharField(max_length=255)
	noOfReplays = models.IntegerField(default=0)
	rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)

class Plays(models.Model):
	game = models.ForeignKey(Games, on_delete=models.CASCADE, null=True)
	replay = models.BooleanField(default=False)
	timeSpentPlaying = models.DurationField(null=True)
	startDate = models.DateField(null=True)
	completedDate = models.DateField(null=True)


class Genres(models.Model):
	name = models.CharField(max_length=255)

