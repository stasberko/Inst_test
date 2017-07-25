from django.shortcuts import render
from .forms import Text
from .models import Textf


# Create your views here.
def txt(reqest):
    form = Text(reqest.POST or None)
    req = Textf.objects.all().order_by('-id')

    return render(reqest, "help.html", {"req": req, 'form': form})
