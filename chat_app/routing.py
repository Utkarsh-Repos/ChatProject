from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/cla/<str:group_name>/', consumers.MyAsyncConsumerChannelLayerDynamicGroupDatabase.as_asgi()),
]