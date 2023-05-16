from django.urls import path
from .views import MessageListCreateAPIView, MessageRetrieveUpdateDestroyAPIView
from .views import ConversationListCreateAPIView, ConversationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('messages/', MessageListCreateAPIView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroyAPIView.as_view(), name='message-retrieve-update-destroy'),
    path('conversation/', ConversationListCreateAPIView.as_view(), name='conversation-list-create'),
    path('conversation/<int:pk>/', ConversationRetrieveUpdateDestroyAPIView.as_view(), name='conversation-retrieve-update-destroy'),
]