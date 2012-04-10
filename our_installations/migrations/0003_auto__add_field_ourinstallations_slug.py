# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OurInstallations.slug'
        db.add_column('our_installations_ourinstallations', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'OurInstallations.slug'
        db.delete_column('our_installations_ourinstallations', 'slug')

    models = {
        'our_installations.ourinstallations': {
            'Meta': {'object_name': 'OurInstallations'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['our_installations']