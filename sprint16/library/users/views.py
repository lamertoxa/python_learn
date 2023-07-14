from django.shortcuts import render
from authentication.models import *
from django.core.exceptions import PermissionDenied

def get_all_users(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    context = {}
    if request.method == 'POST':
        id = request.POST['id']
        if id:
            context['users_list'] = [(CustomUser.get_by_id(id))]
        else:
            context['users_list'] = CustomUser.get_all()
    else:
        context['users_list'] = CustomUser.get_all()
    context['librarian'] = CustomUser.get_by_staff
    return render(request, 'users.html', context=context)

def user_get_one(request, id):
    if not request.user.is_authenticated:
        raise PermissionDenied
    user = CustomUser.get_by_id(id)
    return render(request, 'user_one.html', {"user": user})
