from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Genres

# Create your views here.
def myList(request):
	template = loader.get_template('list.html')
	return HttpResponse(template.render(request=request))

def genreList(request):
	template = loader.get_template('genres.html')
	genreList = Genres.objects.all().values()
	context = {
		'genreList' : genreList,
	}

	return HttpResponse(template.render(context, request))
