from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import People

def people(request):
	data = People.objects.all().values()
	template = loader.get_template('people.html')
	context = {
		'people' : data
	}
	return HttpResponse(template.render(context, request))

def homepage(request):
     template = loader.get_template('main.html')
     return HttpResponse(template.render(request=request))

def details(request, id):
  person = People.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'person': person,
  }
  return HttpResponse(template.render(context, request))