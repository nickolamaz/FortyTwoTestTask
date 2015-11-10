# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HttpRequestStore.is_viewed'
        db.add_column(u't3_middleware_httprequeststore', 'is_viewed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'HttpRequestStore.method'
        db.alter_column(u't3_middleware_httprequeststore', 'method', self.gf('django.db.models.fields.CharField')(default=None, max_length=6))

        # Changing field 'HttpRequestStore.host'
        db.alter_column(u't3_middleware_httprequeststore', 'host', self.gf('django.db.models.fields.CharField')(default=None, max_length=200))

        # Changing field 'HttpRequestStore.date'
        db.alter_column(u't3_middleware_httprequeststore', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None))

        # Changing field 'HttpRequestStore.path'
        db.alter_column(u't3_middleware_httprequeststore', 'path', self.gf('django.db.models.fields.CharField')(default=None, max_length=200))

    def backwards(self, orm):
        # Deleting field 'HttpRequestStore.is_viewed'
        db.delete_column(u't3_middleware_httprequeststore', 'is_viewed')


        # Changing field 'HttpRequestStore.method'
        db.alter_column(u't3_middleware_httprequeststore', 'method', self.gf('django.db.models.fields.CharField')(max_length=6, null=1))

        # Changing field 'HttpRequestStore.host'
        db.alter_column(u't3_middleware_httprequeststore', 'host', self.gf('django.db.models.fields.CharField')(max_length=256, null=1))

        # Changing field 'HttpRequestStore.date'
        db.alter_column(u't3_middleware_httprequeststore', 'date', self.gf('django.db.models.fields.DateTimeField')(null=1))

        # Changing field 'HttpRequestStore.path'
        db.alter_column(u't3_middleware_httprequeststore', 'path', self.gf('django.db.models.fields.CharField')(max_length=256, null=1))

    models = {
        u't3_middleware.httprequeststore': {
            'Meta': {'object_name': 'HttpRequestStore'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_viewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['t3_middleware']