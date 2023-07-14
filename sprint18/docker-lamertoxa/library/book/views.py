from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from book.models import Book
from author.models import Author
from order.models import Order
from django.db.models import Q
from .forms import BookForm
from .forms import BookAuthorForm
from django.http import HttpResponseRedirect as redirect
from django.contrib import messages


def book_get(request):
    context = {}
    if request.method == "GET":
        context['book_list'] = Book.get_all()
    if request.method == "POST":
        search_phrase = request.POST.get("search_phrase")
        q_book = Book.objects.filter(Q(name__contains=search_phrase)
                                       | Q(description__contains=search_phrase)
                                       | Q(id__contains=search_phrase))
        q_author = Author.objects.filter(Q(name__contains=search_phrase)
                                       | Q(surname__contains=search_phrase)
                                       | Q(patronymic__contains=search_phrase))

        q_books_author = Book.objects.filter( Q(authors__in=q_author))
        book_list = (q_books_author | q_book).distinct()
        context['book_list']=book_list
    return render(request,'book.html', context=context)

def book_get_one(request, id):
    book = Book.objects.get(pk=id)
    aut_all = book.authors.all()
    author = ", ".join([f"{i.name} {i.surname} {i.patronymic}" for i in aut_all])
    return render(request, 'book_one.html', {"book":book, "author":author})


def book_form(request, id=0):
    submitted = False
    if request.method == 'GET':
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
            submitted = True
        return render(request, 'book_form.html', {'form':form, 'submitted':submitted})
    else:
        if id == 0:
            form = BookForm(request.POST)
            info = f"New book was successfully created"
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
            info = f"Book with id:{id} was successfully updated"
        if form.is_valid():
            form.save()
            messages.success(request, info)
        return redirect('/book', {'submitted':submitted})

def book_author(request, id):
    context={}
    book = Book.objects.get(pk=id)
    context['book'] = book
    authors = book.authors.all()
    if authors:
        form = BookAuthorForm(initial={'book_author':authors})
    else:
        form = BookAuthorForm(request.POST)
    context['form'] = form
    if request.method == 'GET':
        return render(request, 'book_author.html', context)
    else:
        form = BookAuthorForm(request.POST)
        book.authors.clear()
        book.save()
        for author_id in form['book_author'].value():
            book.update_authors(author_id)
        book.save()
        info = f"Authors for book with id:{id} were successfully updated"
        messages.success(request, info)
        return redirect('/book')
