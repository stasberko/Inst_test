from django import forms
from .models import Textf

class Text(forms.Form):
    text = forms.CharField(widget=forms.Textarea)