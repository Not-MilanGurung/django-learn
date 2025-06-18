from django.urls import path
from . import views

urlpatterns = [
	path('', views.myList, name='MyList'),
	path('genres/', views.genre_list, name='ListOfGenre'),
]
