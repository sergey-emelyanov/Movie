from django.urls import path
from . import views

urlpatterns = [
	path('', views.show_all_books),
	path('<slug:slug_book>', views.show_one_book, name='book-details')
]