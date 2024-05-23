from django.db import models
from django.utils import timezone


class DateTimeMixin(models.Model):
    date_created = models.DateTimeField(default=timezone.now())
    date_updated = models.DateTimeField(default=timezone.now())

    class Meta:
        abstract = True
