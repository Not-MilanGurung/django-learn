from django.contrib import admin
from .models import Genre, Game, Play

class GenresAdmin(admin.ModelAdmin):
	list_display = ('name',)

class GamesAdmin(admin.ModelAdmin):
	list_display = ('name', 'noOfReplays', 'rating')


admin.site.register(Genre, GenresAdmin)
admin.site.register(Game, GamesAdmin)