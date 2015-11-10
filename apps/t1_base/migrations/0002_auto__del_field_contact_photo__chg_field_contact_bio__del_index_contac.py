# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contact.photo'
        db.delete_column(u't1_base_contact', 'photo')


        # Changing field 'Contact.bio'
        db.alter_column(u't1_base_contact', 'bio', self.gf('django.db.models.fields.TextField')(default='Bio'))
        # Removing index on 'Contact', fields ['date_of_birth']
        db.delete_index(u't1_base_contact', ['date_of_birth'])


        # Changing field 'Contact.skype'
        db.alter_column(u't1_base_contact', 'skype', self.gf('django.db.models.fields.CharField')(default='skype_id', max_length=50))

        # Changing field 'Contact.other_contacts'
        db.alter_column(u't1_base_contact', 'other_contacts', self.gf('django.db.models.fields.TextField')(default='contacts'))

    def backwards(self, orm):
        # Adding index on 'Contact', fields ['date_of_birth']
        db.create_index(u't1_base_contact', ['date_of_birth'])

        # Adding field 'Contact.photo'
        db.add_column(u't1_base_contact', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=1, blank=1),
                      keep_default=False)


        # Changing field 'Contact.bio'
        db.alter_column(u't1_base_contact', 'bio', self.gf('django.db.models.fields.TextField')(null=1))

        # Changing field 'Contact.skype'
        db.alter_column(u't1_base_contact', 'skype', self.gf('django.db.models.fields.CharField')(max_length=50, null=1))

        # Changing field 'Contact.other_contacts'
        db.alter_column(u't1_base_contact', 'other_contacts', self.gf('django.db.models.fields.TextField')(null=1))

    models = {
        u't1_base.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['t1_base']