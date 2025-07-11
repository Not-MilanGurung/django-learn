from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Game, Genre, Play

class UserSerializer(serializers.ModelSerializer):
    games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'games']
		
class GameSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Game
		fields = ['name', 'noOfReplays', 'rating', 'genre','owner']

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = ['name']

class PlaySerializer(serializers.ModelSerializer):
	class Meta:
		model = Play
		fields = ['game', 'replay', 'timeSpentPlaying', 'startDate', 'completedDate']
