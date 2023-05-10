from django.db import models
from accounts.models import UserProfile, AstrologerProfile, User

# Create your models here.
class Conversation(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    astrologer = models.ForeignKey(AstrologerProfile, on_delete=models.CASCADE, blank=True, null=True )
    is_active = models.BooleanField(default=True)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.sender.username}"

