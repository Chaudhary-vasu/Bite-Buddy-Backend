from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('users/', UserListAPIView.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    # path('orders/', OrdersListAPIView.as_view(), name='orders-list'),
    # path('orders/<int:pk>/', OrdersDetailAPIView.as_view(), name='orders-detail'),
    path("api/meals-item/", MealsItemAPI.as_view()),
    path("api/orders/<str:user>", OrdersAPI.as_view()),
    path("api/orders/", OrdersAPI.as_view()),
    path("api/meals-item/<str:meal_id>/", MealDetailsAPIView.as_view(), name="meal-details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
