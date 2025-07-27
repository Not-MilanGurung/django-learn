from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length=255, primary_key=True)

	def __str__(self):
		return self.name

class Game(models.Model):
	name = models.CharField(max_length=255, primary_key=True)
	noOfReplays = models.IntegerField(default=0)
	rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
	genre = models.ForeignKey(Genre, null=False, on_delete=models.PROTECT)
	owner = models.ForeignKey('auth.User', related_name='games', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Play(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	replay = models.BooleanField(default=False)
	timeSpentPlaying = models.DurationField(null=True)
	startDate = models.DateField(null=True)
	completedDate = models.DateField(null=True)

	def __str__(self):
		return f'{self.game} {self.startDate}'
	
class Image(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField()

class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# A route to upload jpg, png, webp
# Another route for pdf only
# Check mime type