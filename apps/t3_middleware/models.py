from django.db import models
from datetime import datetime

# Create your models here.


class HttpRequestStore(models.Model):
    date = models.DateTimeField('Request date/time', default=datetime.now())
    method = models.CharField('Method', max_length=6)
    path = models.CharField(max_length=256)
    host = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s %s %s' % (
            self.date.strftime('%Y-%m-%d %H:%M:%S'),
            self.method,
            self.path
        )
