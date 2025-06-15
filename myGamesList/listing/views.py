from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Genre, Game

# Create your views here.
def myList(request):
	template = loader.get_template('list.html')
	gameList = Game.objects.all().values()
	context = {
		'gameList' : gameList
	}
	return HttpResponse(template.render(context, request))

def genreList(request):
	template = loader.get_template('genres.html')
	genreList = Genre.objects.all().values()
	context = {
		'genreList' : genreList,
	}

	return HttpResponse(template.render(context, request))
