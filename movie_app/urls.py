from django.urls import path
from . import views

urlpatterns = [
	path('', views.show_all_movies),
	path('movie/<slug:slug_movie>',views.show_one_movies, name='movie-details')

]