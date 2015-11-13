from django.db import models


class ModelSignal(models.Model):
    action = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s: %s' % (self.action, self.model)
