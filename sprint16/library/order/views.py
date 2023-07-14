from django.shortcuts import render
from order.models import Order
from django.core.exceptions import PermissionDenied
import datetime

def order_get(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    context = {}
    if request.user.is_staff:
        context['order_list'] = Order.get_all()
    else:
        id = request.user.id
        context['order_list'] = Order.objects.filter(user_id=id).all()
    return render(request, 'order.html', context=context)

def order_open(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    context = {}
    if request.method == "POST":
        user_id = request.user.id
        book_id = request.POST.get("book id")
        days = int(request.POST.get("days"))
        due_time = datetime.datetime.now() + datetime.timedelta(days=days)
        new_order = Order(user_id=user_id, book_id=book_id, plated_end_at=due_time)
        new_order.save()
        context['created'] = True
    return render(request, 'order_open.html', context=context)


def order_close(request):
    if not request.user.is_staff:
        raise PermissionDenied
    context = {}
    if request.method == "POST":
        id = request.POST.get("order id")
        order = Order.get_by_id(id)
        if order:
            order.update(end_at=datetime.datetime.now())
            context['closed'] = True
            context['info'] = f"{id} was closed"
        else:
            context['closed'] = True
            context['info'] = f"{id} was not found"
    return render(request, 'order_close.html', context=context)

def order_close_id(request, id):
    if not request.user.is_staff:
        raise PermissionDenied
    context = {}
    order = Order.get_by_id(id)
    order.update(end_at=datetime.datetime.now())
    context['order_list'] = Order.get_all()
    return render(request, 'order.html', context=context)


def order_find(request):
    if not request.user.is_staff:
        raise PermissionDenied
    context = {}
    if request.method == "POST":
        id = request.POST.get("Order ID")
        orders = Order.objects.filter(user_id=id).all()
        context['find'] = True
        context['orders'] = orders
    return render(request, 'order_find.html', context=context)
