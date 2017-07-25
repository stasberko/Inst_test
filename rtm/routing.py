from .consumers import MyConsumer
from .consumers import Demultiplexer
from channels import route, route_class
from .models import TextfBinding

channel_routing = [
    route_class(Demultiplexer, path="^/binding/"),
    route_class(MyConsumer, path=r"^/chat/"),
    # route("websocket.connect", consumers.ws_connect, path=r"^/$"),
]