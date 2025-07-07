from rest_framework import serializers
from .models import Game, Genre

class GameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ['name', 'noOfReplays', 'rating', 'genre']

class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = ['name']