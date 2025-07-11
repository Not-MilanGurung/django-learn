from django.urls import path
from . import views

urlpatterns = [
	path('', views.myList, name='MyList'),
	path('genres/', views.genre_list, name='ListOfGenre'),
	path('addgame/', views.add_game, name="AddGame"),
	path('games/', views.GameList.as_view()),
	path('games/<str:pk>/', views.GameDetail.as_view()),
	path('users/', views.UserList.as_view()),
	path('users/<int:pk>/', views.UserDetail.as_view()),
	path('ex/', views.ExampleView.as_view())
]
