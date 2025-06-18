from django.shortcuts import render, redirect, get_object_or_404
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

def genre_list(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            genre_name = request.POST.get('genre_name')
            if genre_name and not Genre.objects.filter(name=genre_name).exists():
                Genre.objects.create(name=genre_name)

        elif action == 'edit':
            old_name = request.POST.get('old_name')
            new_name = request.POST.get('new_name')
            if old_name and new_name:
                genre = get_object_or_404(Genre, pk=old_name)
                genre.delete()  # Because name is primary key
                Genre.objects.create(name=new_name)

        elif action == 'delete':
            genre_name = request.POST.get('genre_name')
            genre = get_object_or_404(Genre, pk=genre_name)
            genre.delete()

        return redirect('ListOfGenre')

    genres = Genre.objects.all().order_by('name')
    return render(request, 'genres.html', {'genreList': genres})