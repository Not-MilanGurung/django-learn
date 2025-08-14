from django.db import models

class Genre(models.Model):
	name = models.CharField(max_length=128, unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Platform(models.Model):
	name = models.CharField(max_length=128, unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name
	
class StoreFront(models.Model):
	name = models.CharField(max_length=128, unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


class Game(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	release_date = models.DateField(blank=True, null=True)
	developer = models.CharField(max_length= 128, blank=True)
	publisher = models.CharField(max_length= 128, blank=True)
	genres = models.ManyToManyField(Genre, related_name="games", blank=True)
	platforms = models.ManyToManyField(Platform, related_name="games", blank=True)
	owner = models.ForeignKey("auth.User", related_name="games", on_delete=models.CASCADE, null=True, blank=True)
	cover_image = models.ImageField(upload_to="covers/", blank=True, null=True)

	def __str__(self):
		return self.name

class PlayType(models.Model):
	name = models.CharField(max_length=32, unique=True)

	def __str__(self):
		return self.name

class Play(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	platform = models.ForeignKey(Platform, on_delete=models.SET_NULL, null=True)
	storefront = models.ForeignKey(StoreFront, on_delete=models.SET_NULL, null=True)
	play_type = models.ManyToManyField(PlayType)
	time_spent_playing = models.DurationField(null=True)
	note = models.TextField(null=True)
	start_date = models.DateField(null=True)
	completion_date = models.DateField(null=True)
	rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)

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