from django.contrib import admin
from django.urls import path
from .views import create_group_to_chat_within, home_page, show_group, show_client

urlpatterns = [
    path('', home_page, name='home-page'),
    path('create-group/', create_group_to_chat_within, name='create-group'),
    path('show-group/', show_group, name='show-group'),
    path('client/<str:group_name>/', show_client, name='client-server'),

]
