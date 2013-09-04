# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        orm['sushack.Event'].objects.create(
            name = 'Hackday 2',
            description = '',
            where='16 Middle Way, Oxford, OX2 7LH',
            start=datetime.datetime(2012, 8, 18, 9, 30),
            finish=datetime.datetime(2012, 8, 18, 20, 45),
            current=False,
        )

    def backwards(self, orm):
        "Write your backwards methods here."
        pass

    models = {
        u'sushack.attendee': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Attendee'},
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'project': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'github_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'sushack.event': {
            'Meta': {'ordering': "['start']", 'object_name': 'Event'},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'finish': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'where': ('django.db.models.fields.TextField', [], {})
        },
        u'sushack.mailinglistperson': {
            'Meta': {'object_name': 'MailingListPerson'},
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['sushack']
    symmetrical = True
