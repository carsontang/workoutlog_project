# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Workout'
        db.create_table(u'workouts_workout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('workout_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'workouts', ['Workout'])

        # Adding model 'Lift'
        db.create_table(u'workouts_lift', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lift_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'workouts', ['Lift'])

        # Adding model 'Exercise'
        db.create_table(u'workouts_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lift', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workouts.Lift'])),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workouts.Workout'])),
        ))
        db.send_create_signal(u'workouts', ['Exercise'])

        # Adding model 'ExerciseSet'
        db.create_table(u'workouts_exerciseset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workouts.Exercise'])),
            ('number_of_reps', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('number_of_sets', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'workouts', ['ExerciseSet'])


    def backwards(self, orm):
        # Deleting model 'Workout'
        db.delete_table(u'workouts_workout')

        # Deleting model 'Lift'
        db.delete_table(u'workouts_lift')

        # Deleting model 'Exercise'
        db.delete_table(u'workouts_exercise')

        # Deleting model 'ExerciseSet'
        db.delete_table(u'workouts_exerciseset')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'workouts.exercise': {
            'Meta': {'object_name': 'Exercise'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lift': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workouts.Lift']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workouts.Workout']"})
        },
        u'workouts.exerciseset': {
            'Meta': {'object_name': 'ExerciseSet'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workouts.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_reps': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'number_of_sets': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'workouts.lift': {
            'Meta': {'object_name': 'Lift'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lift_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'workouts.workout': {
            'Meta': {'object_name': 'Workout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'workout_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['workouts']