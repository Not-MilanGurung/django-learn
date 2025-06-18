from django.db import models

class Game(models.Model):
	name = models.CharField(max_length=255)
	noOfReplays = models.IntegerField(default=0)
	rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)

	def __str__(self):
		return f'{self.name}'

class Play(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
	replay = models.BooleanField(default=False)
	timeSpentPlaying = models.DurationField(null=True)
	startDate = models.DateField(null=True)
	completedDate = models.DateField(null=True)

	def __str__(self):
		return f'{self.game} {self.startDate}'


class Genre(models.Model):
	name = models.CharField(max_length=255, primary_key=True)

	def __str__(self):
		return f'{self.name}'

