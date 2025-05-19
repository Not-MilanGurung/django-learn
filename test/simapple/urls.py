from django.urls import path
from . import views

urlpatterns = [
	path('simapple/', views.greetings, name="Greetings"),
]