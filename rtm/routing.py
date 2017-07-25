from .consumers import MyConsumer
from channels import route, route_class

channel_routing = [
    route_class(MyConsumer, path=r"^/wss/"),
]