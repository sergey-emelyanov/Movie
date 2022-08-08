from django.shortcuts import render, get_object_or_404
from .models import BookShop


def show_all_books(request):
	books = BookShop.objects.all()
	for book in books:
		book.save()
	return render(request, 'book_app/show_all_books.html', {
		'books': books
	})


def show_one_book(request, slug_book):
	book = get_object_or_404(BookShop, slug=slug_book)
	return render(request, 'book_app/show_one_book.html', {'book': book})
