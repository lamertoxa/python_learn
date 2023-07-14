from django.shortcuts import render,redirect
from book.models import Book
from order.models import Order
from authentication.models import CustomUser
import logging


def all_orders(request):
    if request.method == 'POST':

        id = request.POST['order_id']
        logging.warning(f"{id}")
        Order.delete_by_id(id)
        return redirect("order:all_orders")
    orders = Order.objects.select_related().values('id',
                                                   'book__name',
                                                   'book__id',
                                                   'user__id',
                                                   'user__first_name',
                                                   'created_at',
                                                   'end_at',
                                                   "plated_end_at",)
    for i in orders:
        logging.warning(f"{i}")
    return render(request,"all_orders.html",context={"orders":orders,"title":"All orders"})


def new_orders(request):
    if request.method == 'POST':

        book_id =  request.POST['book_id']
        planed_end = request.POST['planed_end']
        book = Book.get_by_id(book_id)
        logging.warning(f"{book}{planed_end}{request.user.id}")
        my_order = Order(user_id=request.user.id, book=book, plated_end_at = planed_end)
        my_order.save()
        return redirect("order:all_orders")

    books = Book.get_all()
    users = CustomUser.get_all()

    return render(request,context={"books":books,"users":users},template_name="create_order.html")

def my_orders(request):
    orders = Order.objects.select_related().filter(user_id = request.user.id)\
        .values('id',
                'book__name',
                'book__id',
                'created_at',
                'end_at',
                 "plated_end_at",
                )
    return render(request, context={"orders": orders,"title":"My order"}, template_name="my_orders.html")
