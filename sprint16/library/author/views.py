from django.shortcuts import render
from author.models import Author
from django.core.exceptions import PermissionDenied


def author_get(request):
    if not request.user.is_staff:
        raise PermissionDenied
    context = {}
    context['author_list'] = Author.get_all()
    return render(request,'author.html', context=context)

def author_new(request):
    if not request.user.is_staff:
        raise PermissionDenied
    context={}
    if request.method == "POST":
        name = request.POST.get("new_name")
        surname = request.POST.get("new_surname")
        patronymic = request.POST.get("new_patronymic")
        new_author = Author(name=name, surname=surname, patronymic=patronymic)
        new_author.save()
        context['created'] = True
    return render(request,'author_new.html', context=context)

def author_delete(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    context={}
    if request.method == "POST":
        id = request.POST.get("new_ID")
        author = Author.get_by_id(id)
        if author:
            books = author.books.all()
            if books:
                context['deleted'] = True
                context['info'] = f"{id} cant be deleted, since he/she has books"
            else:
                Author.delete_by_id(id)
                context['deleted'] = True
                context['info'] = f"{id} was deleted"
        else:
            context['deleted'] = True
            context['info'] = f"{id} was not found"
    return render(request,'author_delete.html', context=context)

def author_delete_id(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    context = {}
    Author.delete_by_id(id)
    context['author_list'] = Author.get_all()
    return render(request, 'author.html', context=context)
