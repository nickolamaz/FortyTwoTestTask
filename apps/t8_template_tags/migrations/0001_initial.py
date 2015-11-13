# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModelSignal'
        db.create_table(u't8_template_tags_modelsignal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u't8_template_tags', ['ModelSignal'])


    def backwards(self, orm):
        # Deleting model 'ModelSignal'
        db.delete_table(u't8_template_tags_modelsignal')


    models = {
        u't8_template_tags.modelsignal': {
            'Meta': {'object_name': 'ModelSignal'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['t8_template_tags']