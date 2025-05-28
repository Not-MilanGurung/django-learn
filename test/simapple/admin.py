from django.contrib import admin
from .models import People

class PeopleAdmin(admin.ModelAdmin):
	list_display = ("firstName", "lastName")

# Register your models here.
admin.site.register(People, PeopleAdmin)
