from django.db import models
from django.forms import CharField, DateTimeField

class Topic(models.Model):
    Text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
