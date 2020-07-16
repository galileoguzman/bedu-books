from django.shortcuts import render

from .models import Book

# Create your views here.
def home_books(request):
    books = Book.objects.all()
    books_count = books.count()
    return render(request, 'home_books.html',{
        'books': books,
        'count': books_count
    })
