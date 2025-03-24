from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='수정일', auto_now=True)
    class Meta:
        abstract=True