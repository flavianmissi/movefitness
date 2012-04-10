# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'OurInstallation'
        db.delete_table('our_installations_ourinstallation')

        # Adding model 'OurInstallations'
        db.create_table('our_installations_ourinstallations', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('our_installations', ['OurInstallations'])

    def backwards(self, orm):
        # Adding model 'OurInstallation'
        db.create_table('our_installations_ourinstallation', (
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('our_installations', ['OurInstallation'])

        # Deleting model 'OurInstallations'
        db.delete_table('our_installations_ourinstallations')

    models = {
        'our_installations.ourinstallations': {
            'Meta': {'object_name': 'OurInstallations'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['our_installations']