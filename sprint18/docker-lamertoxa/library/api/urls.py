from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'user',views.UserView,basename='user')
router.register(r'author',views.AuthorView,basename='author')
router.register(r'book',views.BookView,basename='book')
router.register(r'order',views.OrderView,basename='order')
router_user = routers.DefaultRouter()

router_user_order = routers.DefaultRouter()
router_user_order.register(r'order',views.UserOrderView,basename='order')

urlpatterns = [
    path(r'v1/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path(r'v1/user/<int:us>/', include(router_user_order.urls)),
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token/refresh/', TokenRefreshView.as_view())

]
