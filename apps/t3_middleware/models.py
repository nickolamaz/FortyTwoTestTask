from django.db import models
from datetime import datetime

# Create your models here.


class HttpRequestStore(models.Model):
    date = models.DateTimeField('Request date/time',
                                default=datetime.now(), null=1, blank=1)
    method = models.CharField('Method', max_length=6, null=1, blank=1)
    path = models.CharField(max_length=256, null=1, blank=1)
    host = models.CharField(max_length=256, null=1, blank=1)
    priority = models.IntegerField(default=1)

    def __unicode__(self):
        return u'%s %s %s' % (
            self.date.strftime('%Y-%m-%d %H:%M:%S'),
            self.method,
            self.path
        )
