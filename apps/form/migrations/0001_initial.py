# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModelForm'
        db.create_table('form_modelform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(related_name='model_forms', to=orm['model.Model'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('form', ['ModelForm'])

        # Adding unique constraint on 'ModelForm', fields ['model', 'name']
        db.create_unique('form_modelform', ['model_id', 'name'])

        # Adding M2M table for field model_fields on 'ModelForm'
        m2m_table_name = db.shorten_name('form_modelform_model_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('modelform', models.ForeignKey(orm['form.modelform'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['modelform_id', 'modelfield_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ModelForm', fields ['model', 'name']
        db.delete_unique('form_modelform', ['model_id', 'name'])

        # Deleting model 'ModelForm'
        db.delete_table('form_modelform')

        # Removing M2M table for field model_fields on 'ModelForm'
        db.delete_table(db.shorten_name('form_modelform_model_fields'))


    models = {
        'application.application': {
            'Meta': {'object_name': 'Application'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': "orm['project.Project']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'field.modelfield': {
            'Meta': {'ordering': "('id',)", 'unique_together': "(('model', 'content_type', 'object_id'),)", 'object_name': 'ModelField'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'model_fields'", 'to': "orm['model.Model']"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'form.modelform': {
            'Meta': {'unique_together': "(('model', 'name'),)", 'object_name': 'ModelForm'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'model_forms'", 'to': "orm['model.Model']"}),
            'model_fields': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['field.ModelField']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'model.model': {
            'Meta': {'object_name': 'Model'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'models'", 'to': "orm['application.Application']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'db_table': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'has_admin_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_form_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_read_only_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'verbose_name_plural': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'project.project': {
            'Meta': {'unique_together': "(('owner', 'name'),)", 'object_name': 'Project'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['auth.User']"}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['model.Model']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['form']