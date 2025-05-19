from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name="Greetings"),
	path('details/<int:id>', views.details, name="Details")
]