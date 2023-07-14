from django.shortcuts import render,redirect
from book.models import Book
from django.db.models import Q
from author.models import Author
import logging
def all_books(request):
    context = {}

    context['books'] = Book.objects.order_by('id').all()

    return render(request, 'books.html', context=context)

def get_book(request, id):
    book = Book.objects.get(id=id)
    authors = book.authors.all()
    author = ", ".join([f"{i.name} {i.surname} {i.patronymic}" for i in authors])
    return render(request, 'about_book.html', {"book":book, "author":author})

def search_book(request):
    context = {}

    if request.method == "POST":

        logging.warning(f"{request.POST}")
        title = request.POST.get("search_book")
        if request.POST.get("author"):
            author_search = Author.objects.filter(Q(name__contains=title) | Q(surname__contains=title))
            context['authors'] = author_search
            context['find'] = True
        if request.POST.get('name') or request.POST.get('description') :
            book_search=Book.objects.filter(Q(name__contains=title) | Q(description__contains=title))
            context['books'] = book_search
            context['find'] = True


    return render(request, 'books.html', context=context)