# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table('contact_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('business_hours', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('contact', ['Contact'])

    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table('contact_contact')

    models = {
        'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'business_hours': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['contact']