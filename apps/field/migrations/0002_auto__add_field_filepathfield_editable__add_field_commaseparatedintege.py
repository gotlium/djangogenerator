# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FilePathField.editable'
        db.add_column('field_filepathfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'CommaSeparatedIntegerField.editable'
        db.add_column('field_commaseparatedintegerfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'XMLField.editable'
        db.add_column('field_xmlfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'OneToOneField.editable'
        db.add_column('field_onetoonefield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ManyToManyField.editable'
        db.add_column('field_manytomanyfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ForeignKeyField.editable'
        db.add_column('field_foreignkeyfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'CharField.editable'
        db.add_column('field_charfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'IPAddressField.editable'
        db.add_column('field_ipaddressfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'FloatField.editable'
        db.add_column('field_floatfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'PositiveIntegerField.editable'
        db.add_column('field_positiveintegerfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'IntegerField.editable'
        db.add_column('field_integerfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'FileField.editable'
        db.add_column('field_filefield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'TextField.editable'
        db.add_column('field_textfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'BigIntegerField.editable'
        db.add_column('field_bigintegerfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'SmallIntegerField.editable'
        db.add_column('field_smallintegerfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'DateField.editable'
        db.add_column('field_datefield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'DecimalField.editable'
        db.add_column('field_decimalfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'PositiveSmallIntegerField.editable'
        db.add_column('field_positivesmallintegerfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'EmailField.editable'
        db.add_column('field_emailfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'NullBooleanField.editable'
        db.add_column('field_nullbooleanfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'BooleanField.editable'
        db.add_column('field_booleanfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'URLField.editable'
        db.add_column('field_urlfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'AutoField.editable'
        db.add_column('field_autofield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'SlugField.editable'
        db.add_column('field_slugfield', 'editable',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FilePathField.editable'
        db.delete_column('field_filepathfield', 'editable')

        # Deleting field 'CommaSeparatedIntegerField.editable'
        db.delete_column('field_commaseparatedintegerfield', 'editable')

        # Deleting field 'XMLField.editable'
        db.delete_column('field_xmlfield', 'editable')

        # Deleting field 'OneToOneField.editable'
        db.delete_column('field_onetoonefield', 'editable')

        # Deleting field 'ManyToManyField.editable'
        db.delete_column('field_manytomanyfield', 'editable')

        # Deleting field 'ForeignKeyField.editable'
        db.delete_column('field_foreignkeyfield', 'editable')

        # Deleting field 'CharField.editable'
        db.delete_column('field_charfield', 'editable')

        # Deleting field 'IPAddressField.editable'
        db.delete_column('field_ipaddressfield', 'editable')

        # Deleting field 'FloatField.editable'
        db.delete_column('field_floatfield', 'editable')

        # Deleting field 'PositiveIntegerField.editable'
        db.delete_column('field_positiveintegerfield', 'editable')

        # Deleting field 'IntegerField.editable'
        db.delete_column('field_integerfield', 'editable')

        # Deleting field 'FileField.editable'
        db.delete_column('field_filefield', 'editable')

        # Deleting field 'TextField.editable'
        db.delete_column('field_textfield', 'editable')

        # Deleting field 'BigIntegerField.editable'
        db.delete_column('field_bigintegerfield', 'editable')

        # Deleting field 'SmallIntegerField.editable'
        db.delete_column('field_smallintegerfield', 'editable')

        # Deleting field 'DateField.editable'
        db.delete_column('field_datefield', 'editable')

        # Deleting field 'DecimalField.editable'
        db.delete_column('field_decimalfield', 'editable')

        # Deleting field 'PositiveSmallIntegerField.editable'
        db.delete_column('field_positivesmallintegerfield', 'editable')

        # Deleting field 'EmailField.editable'
        db.delete_column('field_emailfield', 'editable')

        # Deleting field 'NullBooleanField.editable'
        db.delete_column('field_nullbooleanfield', 'editable')

        # Deleting field 'BooleanField.editable'
        db.delete_column('field_booleanfield', 'editable')

        # Deleting field 'URLField.editable'
        db.delete_column('field_urlfield', 'editable')

        # Deleting field 'AutoField.editable'
        db.delete_column('field_autofield', 'editable')

        # Deleting field 'SlugField.editable'
        db.delete_column('field_slugfield', 'editable')


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
        'field.autofield': {
            'Meta': {'object_name': 'AutoField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.bigintegerfield': {
            'Meta': {'object_name': 'BigIntegerField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.booleanfield': {
            'Meta': {'object_name': 'BooleanField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.charfield': {
            'Meta': {'object_name': 'CharField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'choices': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_length': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unicode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.commaseparatedintegerfield': {
            'Meta': {'object_name': 'CommaSeparatedIntegerField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_length': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.datefield': {
            'Meta': {'object_name': 'DateField'},
            'auto_now': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_now_add': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.datetimefield': {
            'Meta': {'object_name': 'DateTimeField', '_ormbases': ['field.DateField']},
            'datefield_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['field.DateField']", 'unique': 'True', 'primary_key': 'True'})
        },
        'field.decimalfield': {
            'Meta': {'object_name': 'DecimalField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'decimal_places': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_digits': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.emailfield': {
            'Meta': {'object_name': 'EmailField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_length': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.filefield': {
            'Meta': {'object_name': 'FileField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_length': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'upload_to': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.filepathfield': {
            'Meta': {'object_name': 'FilePathField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recursive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.floatfield': {
            'Meta': {'object_name': 'FloatField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.foreignkeyfield': {
            'Meta': {'object_name': 'ForeignKeyField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'related_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['model.Model']"}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.imagefield': {
            'Meta': {'object_name': 'ImageField', '_ormbases': ['field.FileField']},
            'filefield_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['field.FileField']", 'unique': 'True', 'primary_key': 'True'}),
            'height_field': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'width_field': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.integerfield': {
            'Meta': {'object_name': 'IntegerField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.ipaddressfield': {
            'Meta': {'object_name': 'IPAddressField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.manytomanyfield': {
            'Meta': {'object_name': 'ManyToManyField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'related_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['model.Model']"}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.modelfield': {
            'Meta': {'ordering': "('id',)", 'unique_together': "(('model', 'content_type', 'object_id'),)", 'object_name': 'ModelField'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'model_fields'", 'to': "orm['model.Model']"}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'field.nullbooleanfield': {
            'Meta': {'object_name': 'NullBooleanField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.onetoonefield': {
            'Meta': {'object_name': 'OneToOneField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'related_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'relation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['model.Model']"}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.positiveintegerfield': {
            'Meta': {'object_name': 'PositiveIntegerField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.positivesmallintegerfield': {
            'Meta': {'object_name': 'PositiveSmallIntegerField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.slugfield': {
            'Meta': {'object_name': 'SlugField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_length': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.smallintegerfield': {
            'Meta': {'object_name': 'SmallIntegerField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.textfield': {
            'Meta': {'object_name': 'TextField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'field.timefield': {
            'Meta': {'object_name': 'TimeField', '_ormbases': ['field.DateField']},
            'datefield_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['field.DateField']", 'unique': 'True', 'primary_key': 'True'})
        },
        'field.urlfield': {
            'Meta': {'object_name': 'URLField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_length': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'verify_exists': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'field.xmlfield': {
            'Meta': {'object_name': 'XMLField'},
            'blank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'db_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'editable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary_key': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'schema_path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unique': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'verbose_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
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

    complete_apps = ['field']