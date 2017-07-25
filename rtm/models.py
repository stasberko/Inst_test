from django.db import models
from channels.binding.websockets import WebsocketBinding
# Create your models here.

class Textf(models.Model):
    text = models.TextField(max_length=1000)