from django.db import models
from channels.binding.websockets import WebsocketBinding
# Create your models here.

class Textf(models.Model):
    text = models.TextField(max_length=1000)

class TextfBinding(WebsocketBinding):

    model = Textf
    stream = "textstr"
    fields = ["text"]

    @classmethod
    def group_names(cls, instance):
        return ["textstr"]

    def has_permission(self, user, action, pk):
        return True