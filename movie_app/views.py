from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Sum, Min, Max, Avg


def show_all_movies(request):
	movies = Movie.objects.order_by('-rating', '-budget')
	agg = movies.aggregate(Avg("budget"), Max("rating"), Min("rating"))
	return render(request, 'movie_app/show_all_movies.html', {'movies': movies, 'agg': agg})


def show_one_movies(request, slug_movie: str):
	movie = get_object_or_404(Movie, slug=slug_movie)
	return render(request, 'movie_app/show_one_movie.html', {'movie': movie})
