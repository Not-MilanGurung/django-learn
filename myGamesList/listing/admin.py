from django.contrib import admin
from .models import Genre, Game, Play

class GenresAdmin(admin.ModelAdmin):
	list_display = ('name',)

class GamesAdmin(admin.ModelAdmin):
	list_display = ('name', 'noOfReplays', 'rating')

class PlaysAdmin(admin.ModelAdmin):
	list_display = ('game', 'replay', 'timeSpentPlaying', 'startDate', 'completedDate')

admin.site.register(Genre, GenresAdmin)
admin.site.register(Game, GamesAdmin)
admin.site.register(Play, PlaysAdmin)