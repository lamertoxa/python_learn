from django.shortcuts import render
from author.models import Author
from django.core.exceptions import PermissionDenied
from .forms import AuthorForm
from django.http import HttpResponseRedirect as redirect
from django.contrib import messages
from django.db.models import Q

def author_form(request, id=0):
    if not request.user.is_staff:
        raise PermissionDenied
    submitted = False
    if request.method == 'GET':
        if id == 0:
            form = AuthorForm()
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(instance=author)
            submitted = True
        return render(request, 'author_form.html', {'form':form, 'submitted':submitted})
    else:
        if id == 0:
            form = AuthorForm(request.POST)
            info = f"New author was successfully created"
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(request.POST, instance=author)
            info = f"Author with id:{id} was successfully updated"
        if form.is_valid():
            form.save()
            messages.success(request, info)
        return redirect('/author', {'submitted':submitted})

def author_get(request):
    if not request.user.is_staff:
        raise PermissionDenied
    context = {}
    submitted = False
    if request.method == "GET":
        context['author_list'] = Author.get_all()
    if request.method == "POST":
        search_phrase = request.POST.get("search_phrase")
        context['author_list'] = Author.objects.filter(Q(name__contains=search_phrase)
                                                       | Q(surname__contains=search_phrase)
                                                       | Q(patronymic__contains=search_phrase)
                                                       | Q(id__contains=search_phrase))
    return render(request,'author.html', context=context)

def author_delete_id(request, id):
    if not request.user.is_staff:
        raise PermissionDenied
    context = {}
    Author.delete_by_id(id)
    context['author_list'] = Author.get_all()
    messages.success(request, f"Author with id:{id} was successfully deleted")
    return render(request, 'author.html', context=context)
