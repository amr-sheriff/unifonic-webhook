from django.db import models


class Notification(models.Model):
    payload = models.TextField()
