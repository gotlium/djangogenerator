# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Model.get_latest_by'
        db.add_column('model_model', 'get_latest_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='latest_by', null=True, to=orm['field.ModelField']),
                      keep_default=False)

        # Adding field 'Model.managed'
        db.add_column('model_model', 'managed',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Model.ordering'
        db.add_column('model_model', 'ordering',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='order', null=True, to=orm['field.ModelField']),
                      keep_default=False)

        # Adding field 'Model.admin_list_per_page'
        db.add_column('model_model', 'admin_list_per_page',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)

        # Adding field 'Model.admin_list_max_show_all'
        db.add_column('model_model', 'admin_list_max_show_all',
                      self.gf('django.db.models.fields.IntegerField')(default=200),
                      keep_default=False)

        # Adding field 'Model.admin_ordering'
        db.add_column('model_model', 'admin_ordering',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ordering', null=True, to=orm['field.ModelField']),
                      keep_default=False)

        # Adding field 'Model.admin_date_hierarchy'
        db.add_column('model_model', 'admin_date_hierarchy',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='date', null=True, to=orm['field.ModelField']),
                      keep_default=False)

        # Adding field 'Model.admin_inlines'
        db.add_column('model_model', 'admin_inlines',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='inline', null=True, to=orm['application.Application']),
                      keep_default=False)

        # Adding field 'Model.admin_actions_selection_counter'
        db.add_column('model_model', 'admin_actions_selection_counter',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Model.admin_has_add_permission'
        db.add_column('model_model', 'admin_has_add_permission',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Model.admin_has_change_permission'
        db.add_column('model_model', 'admin_has_change_permission',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Model.admin_has_delete_permission'
        db.add_column('model_model', 'admin_has_delete_permission',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding M2M table for field unique_together on 'Model'
        m2m_table_name = db.shorten_name('model_model_unique_together')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field index_together on 'Model'
        m2m_table_name = db.shorten_name('model_model_index_together')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_list_display on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_list_display')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_list_display_links on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_list_display_links')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_list_filter on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_list_filter')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_list_editable on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_list_editable')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_raw_id_fields on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_raw_id_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_readonly_fields on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_readonly_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_filter_horizontal on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_filter_horizontal')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_filter_vertical on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_filter_vertical')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_search_fields on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_search_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_exclude on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_exclude')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])

        # Adding M2M table for field admin_fields on 'Model'
        m2m_table_name = db.shorten_name('model_model_admin_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('model', models.ForeignKey(orm['model.model'], null=False)),
            ('modelfield', models.ForeignKey(orm['field.modelfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['model_id', 'modelfield_id'])


    def backwards(self, orm):
        # Deleting field 'Model.get_latest_by'
        db.delete_column('model_model', 'get_latest_by_id')

        # Deleting field 'Model.managed'
        db.delete_column('model_model', 'managed')

        # Deleting field 'Model.ordering'
        db.delete_column('model_model', 'ordering_id')

        # Deleting field 'Model.admin_list_per_page'
        db.delete_column('model_model', 'admin_list_per_page')

        # Deleting field 'Model.admin_list_max_show_all'
        db.delete_column('model_model', 'admin_list_max_show_all')

        # Deleting field 'Model.admin_ordering'
        db.delete_column('model_model', 'admin_ordering_id')

        # Deleting field 'Model.admin_date_hierarchy'
        db.delete_column('model_model', 'admin_date_hierarchy_id')

        # Deleting field 'Model.admin_inlines'
        db.delete_column('model_model', 'admin_inlines_id')

        # Deleting field 'Model.admin_actions_selection_counter'
        db.delete_column('model_model', 'admin_actions_selection_counter')

        # Deleting field 'Model.admin_has_add_permission'
        db.delete_column('model_model', 'admin_has_add_permission')

        # Deleting field 'Model.admin_has_change_permission'
        db.delete_column('model_model', 'admin_has_change_permission')

        # Deleting field 'Model.admin_has_delete_permission'
        db.delete_column('model_model', 'admin_has_delete_permission')

        # Removing M2M table for field unique_together on 'Model'
        db.delete_table(db.shorten_name('model_model_unique_together'))

        # Removing M2M table for field index_together on 'Model'
        db.delete_table(db.shorten_name('model_model_index_together'))

        # Removing M2M table for field admin_list_display on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_list_display'))

        # Removing M2M table for field admin_list_display_links on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_list_display_links'))

        # Removing M2M table for field admin_list_filter on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_list_filter'))

        # Removing M2M table for field admin_list_editable on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_list_editable'))

        # Removing M2M table for field admin_raw_id_fields on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_raw_id_fields'))

        # Removing M2M table for field admin_readonly_fields on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_readonly_fields'))

        # Removing M2M table for field admin_filter_horizontal on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_filter_horizontal'))

        # Removing M2M table for field admin_filter_vertical on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_filter_vertical'))

        # Removing M2M table for field admin_search_fields on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_search_fields'))

        # Removing M2M table for field admin_exclude on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_exclude'))

        # Removing M2M table for field admin_fields on 'Model'
        db.delete_table(db.shorten_name('model_model_admin_fields'))


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
        'model.model': {
            'Meta': {'object_name': 'Model'},
            'admin_actions_selection_counter': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'admin_date_hierarchy': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'date'", 'null': 'True', 'to': "orm['field.ModelField']"}),
            'admin_exclude': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'exclude'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'admin_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'field'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'admin_filter_horizontal': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'horizontal'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'admin_filter_vertical': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'vertical'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'admin_has_add_permission': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'admin_has_change_permission': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'admin_has_delete_permission': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'admin_inlines': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'inline'", 'null': 'True', 'to': "orm['application.Application']"}),
            'admin_list_display': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'display'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'admin_list_display_links': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'links'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'admin_list_editable': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'editable'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'admin_list_filter': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'filters'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'admin_list_max_show_all': ('django.db.models.fields.IntegerField', [], {'default': '200'}),
            'admin_list_per_page': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'admin_ordering': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ordering'", 'null': 'True', 'to': "orm['field.ModelField']"}),
            'admin_raw_id_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'raw'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'admin_readonly_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'readonly'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'admin_search_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'search'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'models'", 'to': "orm['application.Application']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'db_table': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'get_latest_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'latest_by'", 'null': 'True', 'to': "orm['field.ModelField']"}),
            'has_admin_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_form_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_read_only_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_together': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'index'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'is_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'managed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'order'", 'null': 'True', 'to': "orm['field.ModelField']"}),
            'unique_together': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'uniq'", 'blank': 'True', 'to': "orm['field.ModelField']"}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'verbose_name_plural': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'model.permissions': {
            'Meta': {'object_name': 'Permissions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permissions'", 'to': "orm['model.Model']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'})
        },
        'project.project': {
            'Meta': {'unique_together': "(('owner', 'name'),)", 'object_name': 'Project'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_sys': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['auth.User']"}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['model.Model']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['model']