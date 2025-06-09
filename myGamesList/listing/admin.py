from django.contrib import admin
from .models import Genres

class GenresAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

admin.site.register(Genres, GenresAdmin)