from django.contrib import admin
from .models import Chat, Group


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'timestamp', 'group']


@admin.register(Group)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']