from django.db import models


class HttpRequestStore(models.Model):
    date = models.DateTimeField('Request date/time', auto_now_add=True)
    method = models.CharField('Method', max_length=6)
    path = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    is_viewed = models.BooleanField(default=False)

    priority = models.IntegerField(default=1)

    def __unicode__(self):
        return u'%s %s %s' % (
            self.date.strftime('%Y-%m-%d %H:%M:%S'),
            self.method,
            self.path
        )
