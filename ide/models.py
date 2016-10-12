from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Hits(models.Model):
    date = models.DateField()
    hits = models.BigIntegerField(default=0)

    def __unicode__(self):
        return str(self.date)
