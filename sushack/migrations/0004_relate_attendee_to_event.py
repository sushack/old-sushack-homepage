# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Attendee.event'
        db.add_column(u'refresh_oxford_attendee', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['refresh_oxford.Event']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Attendee.event'
        db.delete_column(u'refresh_oxford_attendee', 'event_id')


    models = {
        u'refresh_oxford.attendee': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Attendee'},
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['refresh_oxford.Event']"}),
            'extra': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'github_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'refresh_oxford.event': {
            'Meta': {'ordering': "['start']", 'object_name': 'Event'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'finish': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'where': ('django.db.models.fields.TextField', [], {})
        },
        u'refresh_oxford.mailinglistperson': {
            'Meta': {'object_name': 'MailingListPerson'},
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['refresh_oxford']