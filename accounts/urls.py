from django.urls import path, include
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView,CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView, AstrologerListCreateAPIView, AstrologerRetrieveUpdateDestroyAPIView, UserLoginView
from . import views

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login' ),
    path('user/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
    path('customer/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customer/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-retrieve-update-destroy'),
    path('astrologer/', AstrologerListCreateAPIView.as_view(), name='astrologer-list-create'),
    path('astrologer/<int:pk>/', AstrologerRetrieveUpdateDestroyAPIView.as_view(), name='astrologer-retrieve-update-destroy'),
]
