from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.files.uploadedfile import UploadedFile
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import magic
from .models import Game, Genre, Play, Image, PDFDocument

class UserSerializer(serializers.ModelSerializer):
	games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all())
	class Meta:
		model = User
		fields = ['id', 'username', 'games']
		
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

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

ALLOWED_IMAGE_MIME_TYPES = [
    'image/png',
    'image/jpeg',
    'image/webp',
]

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ['id','title', 'image']

	def validate_image(self, value : UploadedFile):
		if value.content_type not in ALLOWED_IMAGE_MIME_TYPES:
			raise serializers.ValidationError("Invalid image type. Only PNG, JPEG, and WEBP are allowed.")
		return value

class PDFDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDocument
        fields = ['id', 'title', 'file', 'uploaded_at']

    def validate_file(self, file):
        mime = magic.from_buffer(file.read(2048), mime=True)
        file.seek(0)  # reset file pointer after reading
        if mime != 'application/pdf':
            raise serializers.ValidationError("Uploaded file is not a valid PDF.")
        return file
