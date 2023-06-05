from django.urls import path, include
from .views import CustomerViewSet, UserViewSet,AstrologerViewSet
from . import views

urlpatterns = [

    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),
    path('users/login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),

    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('customers/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),

    path('astrologers/', AstrologerViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('astrologers/<int:pk>/', AstrologerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),

]
