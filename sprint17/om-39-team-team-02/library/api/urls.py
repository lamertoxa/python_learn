from django.urls import path, include
from  . import views
from rest_framework import routers

router_user = routers.DefaultRouter()
router_user.register(r'user',views.UserView,basename='user')
router_user.register(r'order',views.OrderView,basename='order')
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router_user_order = routers.DefaultRouter()
router_user_order.register(r'order',views.UserOrderView,basename='order')


urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token/refresh/', TokenRefreshView.as_view()),
    path(r'v1/',include(router_user.urls)),
    path(r'v1/user/<int:us>/',include(router_user_order.urls))
]
