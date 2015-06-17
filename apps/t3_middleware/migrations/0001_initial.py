# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HttpRequestStore'
        db.create_table(u't3_middleware_httprequeststore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 6, 17, 0, 0))),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u't3_middleware', ['HttpRequestStore'])


    def backwards(self, orm):
        # Deleting model 'HttpRequestStore'
        db.delete_table(u't3_middleware_httprequeststore')


    models = {
        u't3_middleware.httprequeststore': {
            'Meta': {'object_name': 'HttpRequestStore'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 6, 17, 0, 0)'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['t3_middleware']