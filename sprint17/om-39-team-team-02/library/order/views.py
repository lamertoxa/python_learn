from django.shortcuts import render
from .models import Order
from authentication.models import CustomUser as User
from book.models import Book
from django.core.exceptions import PermissionDenied
import datetime
from .forms import OrderForm
from django.http import HttpResponseRedirect as redirect
from django.contrib import messages
from django.db.models import Q
from django.forms.widgets import HiddenInput


def order_get(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    context = {}
    if request.method == "GET":
        if request.user.is_staff:
            context['order_list'] = Order.get_all()
        else:
            id = request.user.id
            context['order_list'] = Order.objects.filter(user_id=id).all()

    if request.method == "POST":
        search_phrase = request.POST.get("search_phrase")
        q_book = Book.objects.filter(Q(name__contains=search_phrase))

        q_user = User.objects.filter(Q(email__contains=search_phrase)
                                     | Q(first_name__contains=search_phrase)
                                     | Q(middle_name__contains=search_phrase)
                                     | Q(last_name__contains=search_phrase))

        q_order = Order.objects.filter(Q(book__in=q_book) | Q(user__in=q_user) | Q(id__contains=search_phrase))

        if request.user.is_staff:
            context['order_list'] = q_order

        else:
            id = request.user.id
            user_q_list = q_order.filter(user_id=id)
            context['order_list'] = user_q_list

    return render(request, 'order.html', context=context)


def order_form(request, id=0):
    if not request.user.is_authenticated:
        raise PermissionDenied
    submitted = False

    if request.method == 'GET':
        if id == 0:
            form = OrderForm(user=request.user)
            user = form._user
            form = OrderForm(user=request.user, initial={'user': user})
            if not user.is_staff:
                form.fields['user'].widget = HiddenInput()
        else:
            order = Order.objects.get(pk=id)
            time = order.plated_end_at
            form = OrderForm(instance=order, user=request.user, initial={'plated_end_at': time})
            submitted = True
        return render(request, 'order_form.html', {'form':form, 'submitted':submitted})

    else:
        if id == 0:
            form = OrderForm(request.POST, user=request.user)
            info = f"New order was successfully created"
            if form.is_valid():
                book_id = form['book'].value()
                book = Book.objects.get(pk=book_id)
                book.count -= 1
                book.save()
        else:
            order = Order.objects.get(pk=id)
            form = OrderForm(request.POST, instance=order, user=request.user)
            info = f"Order with id:{id} was successfully updated"
        if form.is_valid():
            form.save()
            messages.success(request, info)
        return redirect('/order', {'submitted':submitted})


def order_close_id(request, id):
    if not request.user.is_staff:
        raise PermissionDenied
    context = {}
    order = Order.objects.get(pk=id)
    order.close()
    context['order_list'] = Order.get_all()
    return render(request, 'order.html', context=context)
