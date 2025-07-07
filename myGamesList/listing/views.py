from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from rest_framework import viewsets, permissions, views, status
from rest_framework.response import Response
from .models import Genre, Game
from .serializers import GameSerializer, GenreSerializer

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

class GameViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]
        
class GenreViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GameList(views.APIView):
    """
    List all snippets, or create a new game.
    """
    def get(self, request, format=None):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GameDetail(views.APIView):
    """
    Retrieve, update or delete a game instance.
    """
    def get_object(self, name):
        try:
            return Game.objects.get(pk=name)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        game = self.get_object(name)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        game = self.get_object(name)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        game = self.get_object(name)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)