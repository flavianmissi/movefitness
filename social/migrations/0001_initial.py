# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Social'
        db.create_table('social_social', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('social_networking', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('profile', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('social', ['Social'])

    def backwards(self, orm):
        # Deleting model 'Social'
        db.delete_table('social_social')

    models = {
        'social.social': {
            'Meta': {'object_name': 'Social'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'social_networking': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['social']