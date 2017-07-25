from channels.generic.websockets import WebsocketConsumer
from channels.generic.websockets import WebsocketDemultiplexer
from .models import TextfBinding

class Demultiplexer(WebsocketDemultiplexer):

    consumers = {
        "textstr": TextfBinding.consumer,
    }

    def connection_groups(self):
        return ["textstr-updates"]



class MyConsumer(WebsocketConsumer):

    # Set to True to automatically port users from HTTP cookies
    # (you don't need channel_session_user, this implies it)
    http_user = True

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
        # Simple echo
        self.send(text=text, bytes=bytes)

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        pass

# class MyWebsocketConsumer(WebsocketConsumer):
#     def connection_groups(self, **kwargs):
#         """
#         Возвращает список групп для подключения/удаления подключенных участников
#         """
#         return ['general_group']
#     def connect(self, message, **kwargs):
#         """
#         Срабатывает при старте соединения по WebSocket
#         """
#         pass
#     def receive(self, text=None, bytes=None, **kwargs):
#         """
#         Срабатывает, когда приходит сообщение в WebSocket
#         """
#         # Echo
#         self.send(text=text, bytes=bytes)
#     def disconnect(self, message, **kwargs):
#         """
#         Срабатывает при разрыве соединения
#         """
#         pass
