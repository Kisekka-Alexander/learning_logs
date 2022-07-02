from dataclasses import fields
from django import forms
from .models import Topic

class TopiForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields=['text']
        labels = {'text':''}