from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Greetings

def greetings(request):
	greetings = Greetings.objects.all().values()
	template = loader.get_template('hello.html')
	context = {
		'allGreetings' : greetings
	}
	return HttpResponse(template.render(context, request))