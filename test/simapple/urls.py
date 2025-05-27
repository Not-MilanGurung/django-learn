from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name="HomePage"),
	path('people/', views.people, name="People"),
	path('people/details/<int:id>', views.details, name="Details")
]