from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'games', views.GameViewSet, 'games')
router.register(r'genre', views.GenreViewSet, 'genre')

urlpatterns = [
	path('', views.myList, name='MyList'),
	path('genres/', views.genre_list, name='ListOfGenre'),
	path('addgame/', views.add_game, name="AddGame"),
	path('api/', include(router.urls)),
	path('games/', views.GameList.as_view()),
	path('games/<str:name>/', views.GameDetail.as_view())
]
