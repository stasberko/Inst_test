from channels.generic.websockets import WebsocketConsumer
from .forms import Textf
import json


class MyConsumer(WebsocketConsumer):
    # Set to True to automatically port users from HTTP cookies
    # (you don't need channel_session_user, this implies it)
    http_user = True
    channel_session_user = True
    # Set to True if you want it, else leave it out
    strict_ordering = False

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return ["test"]

    def connect(self, message, **kwargs):
        """
        Perform things on connection start
        """
        # Accept the connection; this is done by default if you don't override
        # the connect function.
        self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        """
        Called when a message is received with either text or bytes
        filled out.
        """
        res = Textf(text=text)
        res.save()
        print(self.message.user)
        print(self.message.content)
        print(self.message.reply_channel.name)
        self.send(json.dumps({'message': text}, ensure_ascii=False))

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        print('[CLOSE]')