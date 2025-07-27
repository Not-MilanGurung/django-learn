from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from rest_framework import views, generics, permissions, authentication, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .models import Genre, Game, Image, PDFDocument
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from myGamesList.settings import ACCESS_TOKEN_LIFETIME, REFRESH_TOKEN_LIFETIME


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
	
class GenreListPage(views.APIView):
	renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
	authentication_classes = [JWTAuthentication]
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	template_name = "genres.html"

	def get(self, request, *args, **kwargs):
		genres = Genre.objects.all()
		if request.accepted_renderer.format == 'html':
			return Response({'genreList': genres})
		
		serializer = GenreSerializer(genres, many=True)
		return Response(serializer.data)
	
	def post(self, request, *args, **kwargs):
		serializer = GenreSerializer(data=request.data)
		response = self.get(request, *args, **kwargs)
		if serializer.is_valid():
			serializer.save()
			response.status_code = status.HTTP_201_CREATED
		else: 
			response.status_code = status.HTTP_400_BAD_REQUEST
		return response
	
	def delete(self, request,pk, *args, **kwargs):
		genre_name = request.DELETE.get('name')
		print(genre_name)
		genre = get_object_or_404(Genre, pk=genre_name)
		genre.delete()
		response = self.get(request, *args, **kwargs)
		response.status_code = status.HTTP_204_NO_CONTENT
		return response

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	authentication_classes = [JWTAuthentication]

	def delete(self, request, *args, **kwargs):
		return super().delete(request, *args, **kwargs)

class GameListPage(views.APIView):
	renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
	authentication_classes = [JWTAuthentication]
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	template_name = "list.html"

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	def get(self, request, *args, **kwargs):
		games = Game.objects.all()
		genres = Genre.objects.all()
		if request.accepted_renderer.format == 'html':
			return Response({'gameList' : games, 'genreList': genres})
		
		serializer = GameSerializer(games, many=True)
		return Response(serializer.data)
	
	def post(self, request, *args, **kwargs):
		serializer = GameSerializer(data=request.data)
		response = self.get(request, *args, **kwargs)
		if serializer.is_valid():
			serializer.save()
			response.status_code = status.HTTP_201_CREATED
		else: 
			response.status_code = status.HTTP_400_BAD_REQUEST
		return response

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	authentication_classes = [JWTAuthentication]
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,
							IsOwnerOrReadOnly]
				
class RegisterUser(views.APIView):
	queryset = User.objects.all()
	serializer_class = RegisterSerializer
	permission_classes = [permissions.AllowAny]
	renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
	authentication_classes = [JWTAuthentication]
	template_name = "auth/register.html"

	def get(self, request, *args, **kwargs):
		return Response()
	
	def post(self, request, *args, **kwargs):
		serializer = RegisterSerializer(data=request.data)
		response = self.get(request, *args, **kwargs)
		if serializer.is_valid():
			serializer.save()
			response.status_code = status.HTTP_201_CREATED
		else: 
			response.status_code = status.HTTP_400_BAD_REQUEST
		return response


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]

class ImageList(generics.ListCreateAPIView):
	permission_classes = [permissions.AllowAny]
	queryset = Image.objects.all()
	serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer
	permission_classes = [permissions.AllowAny]

class PDFList(generics.ListCreateAPIView):
	permission_classes = [permissions.AllowAny]
	queryset = PDFDocument.objects.all()
	serializer_class = PDFDocumentSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	
class CookieLoginView(TokenObtainPairView):
	authentication_classes = [JWTAuthentication]
	renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
	permission_classes = [permissions.AllowAny]
	template_name = 'auth/login.html'

	def post(self, request, *args, **kwargs): # type: ignore
        # Call the parent post() to validate credentials
		response = super().post(request, *args, **kwargs)

		if response.status_code == 200:
			access_token = response.data.get("access") # type: ignore
			refresh_token = response.data.get("refresh") # type: ignore

			response.set_cookie(
				key="access_token",
				value=access_token,
				httponly=True,
				secure=True,  # Set to True with HTTPS in production
				samesite="Lax",
				expires=timezone.now() + ACCESS_TOKEN_LIFETIME,
			)
			response.set_cookie(
				key="refresh_token",
				value=refresh_token,
				httponly=True,
				secure=True,
				samesite="Lax",
				expires=timezone.now() + REFRESH_TOKEN_LIFETIME,
			)

			response.status_code = status.HTTP_200_OK
		else:
			response.status_code = status.HTTP_400_BAD_REQUEST
		return response

	
	def get(self, request, *args, **kwargs):
		return Response()
	

class CookieLogoutView(views.APIView):
	def post(self, request):
		refresh = request.COOKIES.get("refresh_token")
		access = request.COOKIES.get("access_token")
		if refresh:
			try:
				token = RefreshToken(refresh)
				token.blacklist()  # Requires token_blacklist app enabled
			except Exception:
				pass  # Silently fail if already blacklisted

		response = redirect("login")
		response.delete_cookie("access_token")
		response.delete_cookie("refresh_token")
		return response
	
class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        request.data['refresh'] = request.COOKIES.get('refresh_token') # type: ignore
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            access_token = response.data.get("access")	# type: ignore
            response.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=True,
                samesite="Lax",
                expires=timezone.now() + timedelta(minutes=15),
            )
            response.data = {"detail": "Token refreshed"}
        return response