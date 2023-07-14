import logging

from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from book.models import Book
from author.models import Author
from order.models import Order
from django.db.models import Q
from .forms import ChangeBookForm


def book_get(request):
    context = {}
    context['book_list'] = Book.get_all()
    return render(request, 'book.html', context=context)

def book_get_one(request, id,change=None):

    book = Book.objects.get(pk=id)
    aut_all = book.authors.all()

    author = ", ".join([f"{i.name} {i.surname} {i.patronymic}" for i in aut_all])
    if change == "change":
        # form = ChangeBookForm(data=request.POST, book_author=book.authors,book_namer=book.name,count=book.count,description=book.description)

        form = ChangeBookForm(authors=Author.objects.all(),choices=aut_all)

        return render(request, 'book_one.html', {"book":book,"form": form})
    return render(request, 'book_one.html', {"book":book, "author":author})



def book_find(request):
    context = {}
    if request.method == "POST":
        search_phrase = request.POST.get("search_phrase")
        option = str(request.POST.get("options"))
        if option == "title":
            book_search = Book.objects.filter(name__contains=search_phrase).all()
        elif option == "author":
            authors = Author.objects.filter(Q(name__contains=search_phrase) | Q(surname__contains=search_phrase) | Q(patronymic__contains=search_phrase))
            book_search = Book.objects.filter(authors__in=authors)
        elif option == "description":
            book_search = Book.objects.filter(description__contains=search_phrase).all()
        context['find'] = True
        context['books'] = book_search
        context['options'] = option
    return render(request, 'book_find.html', context=context)


def book_id_find(request):
    if not request.user.is_staff:
        raise PermissionDenied
    context = {}
    if request.method == "POST":
        id = request.POST.get("Order ID")
        books = Order.objects.filter(user_id=id).all()
        context['find'] = True
        context['books'] = books
    return render(request, 'book_find_id.html', context=context)
