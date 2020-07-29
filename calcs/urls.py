"""Defines URL patterns for calcs."""

from django.urls import path

from . import views

app_name = 'calcs'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	path('pipeflow/', views.pipeflow, name='pipeflow'),
	path('uvsize/', views.uvsize, name='uvsize'),
	]