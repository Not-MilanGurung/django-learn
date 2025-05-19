from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import People

def homepage(request):
	data = People.objects.all().values()
	template = loader.get_template('hello.html')
	context = {
		'people' : data
	}
	return HttpResponse(template.render(context, request))

def details(request, id):
  person = People.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'person': person,
  }
  return HttpResponse(template.render(context, request))