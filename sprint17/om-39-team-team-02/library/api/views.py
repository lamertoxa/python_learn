import logging
from rest_framework import mixins,viewsets, permissions

from .serializers import UserSerializer, OrderUserSerializer,OrderSerializer
from authentication.models import CustomUser
from order.models import Order


class UserReadLibrarianAll(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        return False

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if not request.user.is_authenticated and request.method in ["GET","POST","OPTIONS","HEAD"]:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.user.is_authenticated and request.method in ["DEL","PUT","PATCH"]:
            return True
        return False



class UserView(viewsets.ModelViewSet):
    permission_classes = (UserPermission,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



# class UserOrderView(viewsets.ModelViewSet):
class UserOrderView(
                   mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (UserReadLibrarianAll,)
    serializer_class = OrderUserSerializer

    def get_queryset(self):
        logging.warning(f"{self.kwargs}")
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











