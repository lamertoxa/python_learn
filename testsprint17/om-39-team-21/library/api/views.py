from rest_framework import mixins, viewsets, permissions
from .serializers import UserSerializer
from .serializers import BookSerializer
from .serializers import AuthorSerializer
from .serializers import OrderUserSerializer, OrderSerializer
from authentication.models import CustomUser
from book.models import Book
from author.models import Author
from order.models import Order
from rest_framework import  serializers

class UserReadLibrarianAll(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        return False

class UserView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAdminUser, )

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (UserReadLibrarianAll,)

class UserOrderView(
                   mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = OrderUserSerializer

    def get_queryset(self):

        pk = self.kwargs.get('pk')
        us = self.kwargs.get('us')
        if not pk:
            return Order.objects.filter(user_id=us)
        return Order.objects.filter(pk=pk)

class OrderView(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (UserReadLibrarianAll,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):

        pk = self.request.user.id
        if not self.request.user.is_staff:
            return Order.objects.filter(user_id=pk)
        return Order.objects.all()
