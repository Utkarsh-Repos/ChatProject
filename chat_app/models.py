from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)

class Chat(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_chat')
