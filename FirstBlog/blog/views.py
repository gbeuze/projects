# Create your views here.
from django.db import models

class posts(models.Model):
  author = models.CharFiels(max_length = 30)
  title = models.Charfield(max_length = 100)
  bodytext = models.TextField()
  timestamp = models.DateTimeField()

