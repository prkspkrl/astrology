from django.db import models
from accounts.models import Customer, Astrologer, User
from django.db.models import OneToOneField



# Create your models here.
class Conversation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    astrologer = models.ForeignKey(Astrologer, on_delete=models.CASCADE, null=True,blank=True )
    is_active = models.BooleanField(default=True)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    translated_text = models.TextField(null=True,blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.sender.username}"

