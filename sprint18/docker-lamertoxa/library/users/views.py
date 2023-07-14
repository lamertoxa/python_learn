from django.shortcuts import render
from authentication.models import *
from django.core.exceptions import PermissionDenied
from django.db.models import Q

def get_all_users(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    context = {}
    if request.method == 'POST':
        search_phrase = request.POST['search_phrase']

        q_user = CustomUser.objects.filter(Q(first_name__contains=search_phrase)
                                          | Q(last_name__contains=search_phrase)
                                          | Q(middle_name__contains=search_phrase)
                                          | Q(email__contains=search_phrase)
                                          | Q(id__contains=search_phrase))
        context['users_list'] = q_user
    else:
        context['users_list'] = CustomUser.get_all()
    context['librarian'] = CustomUser.get_by_staff
    return render(request, 'users.html', context=context)


def user_get_one(request, id):
    if not request.user.is_authenticated:
        raise PermissionDenied
    user = CustomUser.get_by_id(id)
    return render(request, 'user_one.html', {"user": user})
