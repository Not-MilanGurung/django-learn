from django.urls import path
from . import views

urlpatterns = [
	path('games/', views.GameListPage.as_view(), name='MyList'),
	path('genres/', views.GenreListPage.as_view(), name='ListOfGenre'),
	path('genres/<str:pk>/', views.GenreDetail.as_view()),
	path('games/<str:pk>/', views.GameDetail.as_view()),
	path('users/', views.UserList.as_view()),
	path('users/<int:pk>/', views.UserDetail.as_view()),
	path('image/', views.ImageList.as_view(), name="image"),
	path('image/<int:pk>', views.ImageDetail.as_view()),
	path('pdf/', views.PDFList.as_view(), name="pdf"),
]
urlpatterns += [
	path('login/', views.CookieLoginView.as_view(), name="login"),
	path('logout/', views.CookieLogoutView.as_view(), name="logout"),
	path('register/', views.RegisterUser.as_view(), name="register"),
]