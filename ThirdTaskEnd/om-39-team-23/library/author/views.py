from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.template.response import TemplateResponse
from .models import Author


def all_authors(request):
    '''Shows all authors'''
    authors = Author.objects.all()
    context = {'authors': authors}


    return render(request, 'authors.html', context=context)



def create(request):
    """Add new author to DB"""
    if request.method == "POST":
        Author.create(name=request.POST.get("name"),surname=request.POST.get("name"),patronymic=request.POST.get("patronymic"))

    return HttpResponseRedirect("/")
    #return render(request, 'author/authors.html')

# def edit(request, id):
#     """Edit authors"""
#     try:
#         author = Author.objects.get(id=id)
#
#         if request.method == "POST":
#             author.name = request.POST.get("name")
#             author.surname = request.POST.get("surname")
#             author.patronymic= request.POST.get("patronymic")
#             #author.books=request.POST.get("books")
#             author.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "author/edit.html", {"author": author})
#     except Author.DoesNotExist:
#         return HttpResponseNotFound("<h2>Author not found</h2>")


def delete(request, id):
    """Delete author from DB"""
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Author not found</h2>")

