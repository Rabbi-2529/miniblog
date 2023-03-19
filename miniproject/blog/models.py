from django.db import models


class upload(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)