from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import viewsets, views, status, generics, permissions, authentication
from rest_framework.response import Response
from .models import Genre, Game
from .serializers import GameSerializer, GenreSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.
def myList(request):
	if request.method == 'POST':
		action = request.POST.get('action')
        
		if action == 'delete':
			game_name = request.POST.get('game_name')
			print(game_name)
			game = get_object_or_404(Game, pk=game_name)
			game.delete()

		return redirect('MyList')
               
	gameList = Game.objects.all().values()
	context = {
		'gameList' : gameList
	}
	return render(request, 'list.html', context)

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

def add_game(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        genre_name = request.POST.get('genre')
        no_of_replays = request.POST.get('no_of_replays')
        rating = request.POST.get('rating')

        if name and genre_name and no_of_replays and rating:
            try:
                genre = Genre.objects.get(name=genre_name)
                Game.objects.create(
                    name=name,
                    genre=genre,
                    noOfReplays=int(no_of_replays),
                    rating=float(rating)
                )
                return redirect('MyList')  # or wherever your game list is
            except Genre.DoesNotExist:
                return render(request, 'add_game.html', {
                    'error': 'Genre not found',
                    'genres': Genre.objects.all()
                })

    return render(request, 'add_game.html', {
        'genres': Genre.objects.all()
    })
    
class GameList(generics.ListCreateAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
							IsOwnerOrReadOnly]
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ExampleView(views.APIView):
    authentication_classes = [authentication.SessionAuthentication, authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)