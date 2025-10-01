from django.contrib import admin
from .models import Genre, Platform, StoreFront, PlayType, Game

class GenresAdmin(admin.ModelAdmin):
	list_display = ("name",)

class PlatformAdmin(admin.ModelAdmin):
	list_display = ("name",)

class StoreFrontAdmin(admin.ModelAdmin):
	list_display = ("name",)

class PlayTypeAdmin(admin.ModelAdmin):
	list_display = ("name",)

class GamesAdmin(admin.ModelAdmin):
	list_display = ("name", "release_date")


admin.site.register(Genre, GenresAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(StoreFront, StoreFrontAdmin)
admin.site.register(PlayType, PlayTypeAdmin)
admin.site.register(Game, GamesAdmin)