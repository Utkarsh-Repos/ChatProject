from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
import json

from channels.exceptions import StopConsumer

from .models import Group, Chat

class MyAsyncConsumerChannelLayerDynamicGroupDatabase(AsyncConsumer):
    async def websocket_connect(self, event):
        print('websocket connect ....', event)
        print('channel layer ....', self.channel_layer)
        print('channel layer ....', self.channel_name)

        self.group_name = self.scope['url_route']['kwargs']['group_name']
        #self.scope is jst like request in views
        print('channel layer scope ....', self.scope['url_route']['kwargs']['group_name'])

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('websocket message receive from client >>>>>>.', event)
        data = json.loads(event['text'])
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        chat = Chat(content=data['msg'],
                    group=group)
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(self.group_name,({
            "type": "chat.message",
            "message": event['text']
        }))

    async def chat_message(self, event):
        print('event chat mssg>>>>>>>', event)
        print('event chat mssg>>>>>>>', event['message'])
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })
    async def websocket_disconnect(self, event):
        print('websocket disconnect ....', event)
        print('channel layer ....', self.channel_layer)
        print('channel layer ....', self.channel_name)
        #to discard channel from group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()

