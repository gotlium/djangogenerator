# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModelField'
        db.create_table('field_modelfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(related_name='model_fields', to=orm['model.Model'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('field', ['ModelField'])

        # Adding unique constraint on 'ModelField', fields ['model', 'content_type', 'object_id']
        db.create_unique('field_modelfield', ['model_id', 'content_type_id', 'object_id'])

        # Adding model 'OneToOneField'
        db.create_table('field_onetoonefield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('related_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['model.Model'])),
        ))
        db.send_create_signal('field', ['OneToOneField'])

        # Adding model 'ForeignKeyField'
        db.create_table('field_foreignkeyfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('related_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['model.Model'])),
        ))
        db.send_create_signal('field', ['ForeignKeyField'])

        # Adding model 'ManyToManyField'
        db.create_table('field_manytomanyfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('related_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('relation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['model.Model'])),
        ))
        db.send_create_signal('field', ['ManyToManyField'])

        # Adding model 'CharField'
        db.create_table('field_charfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unicode', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('choices', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('max_length', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=255)),
        ))
        db.send_create_signal('field', ['CharField'])

        # Adding model 'TextField'
        db.create_table('field_textfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['TextField'])

        # Adding model 'AutoField'
        db.create_table('field_autofield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['AutoField'])

        # Adding model 'BigIntegerField'
        db.create_table('field_bigintegerfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['BigIntegerField'])

        # Adding model 'BooleanField'
        db.create_table('field_booleanfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['BooleanField'])

        # Adding model 'CommaSeparatedIntegerField'
        db.create_table('field_commaseparatedintegerfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('max_length', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=255)),
        ))
        db.send_create_signal('field', ['CommaSeparatedIntegerField'])

        # Adding model 'DateField'
        db.create_table('field_datefield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('auto_now', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('auto_now_add', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['DateField'])

        # Adding model 'DateTimeField'
        db.create_table('field_datetimefield', (
            ('datefield_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['field.DateField'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('field', ['DateTimeField'])

        # Adding model 'DecimalField'
        db.create_table('field_decimalfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('max_digits', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=5)),
            ('decimal_places', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2)),
        ))
        db.send_create_signal('field', ['DecimalField'])

        # Adding model 'EmailField'
        db.create_table('field_emailfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('max_length', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=75)),
        ))
        db.send_create_signal('field', ['EmailField'])

        # Adding model 'FileField'
        db.create_table('field_filefield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('max_length', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=100)),
            ('upload_to', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('field', ['FileField'])

        # Adding model 'FilePathField'
        db.create_table('field_filepathfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('match', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('recursive', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['FilePathField'])

        # Adding model 'FloatField'
        db.create_table('field_floatfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['FloatField'])

        # Adding model 'ImageField'
        db.create_table('field_imagefield', (
            ('filefield_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['field.FileField'], unique=True, primary_key=True)),
            ('height_field', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('width_field', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('field', ['ImageField'])

        # Adding model 'IntegerField'
        db.create_table('field_integerfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['IntegerField'])

        # Adding model 'IPAddressField'
        db.create_table('field_ipaddressfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['IPAddressField'])

        # Adding model 'NullBooleanField'
        db.create_table('field_nullbooleanfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['NullBooleanField'])

        # Adding model 'PositiveIntegerField'
        db.create_table('field_positiveintegerfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['PositiveIntegerField'])

        # Adding model 'PositiveSmallIntegerField'
        db.create_table('field_positivesmallintegerfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['PositiveSmallIntegerField'])

        # Adding model 'SlugField'
        db.create_table('field_slugfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('max_length', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=50)),
        ))
        db.send_create_signal('field', ['SlugField'])

        # Adding model 'SmallIntegerField'
        db.create_table('field_smallintegerfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('field', ['SmallIntegerField'])

        # Adding model 'TimeField'
        db.create_table('field_timefield', (
            ('datefield_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['field.DateField'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('field', ['TimeField'])

        # Adding model 'URLField'
        db.create_table('field_urlfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('max_length', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=200)),
            ('verify_exists', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('field', ['URLField'])

        # Adding model 'XMLField'
        db.create_table('field_xmlfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('verbose_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('null', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('blank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('primary_key', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('db_index', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('schema_path', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('field', ['XMLField'])


    def backwards(self, orm):
        # Removing unique constraint on 'ModelField', fields ['model', 'content_type', 'object_id']
        db.delete_unique('field_modelfield', ['model_id', 'content_type_id', 'object_id'])

        # Deleting model 'ModelField'
        db.delete_table('field_modelfield')

        # Deleting model 'OneToOneField'
        db.delete_table('field_onetoonefield')

        # Deleting model 'ForeignKeyField'
        db.delete_table('field_foreignkeyfield')

        # Deleting model 'ManyToManyField'
        db.delete_table('field_manytomanyfield')

        # Deleting model 'CharField'
        db.delete_table('field_charfield')

        # Deleting model 'TextField'
        db.delete_table('field_textfield')

        # Deleting model 'AutoField'
        db.delete_table('field_autofield')

        # Deleting model 'BigIntegerField'
        db.delete_table('field_bigintegerfield')

        # Deleting model 'BooleanField'
        db.delete_table('field_booleanfield')

        # Deleting model 'CommaSeparatedIntegerField'
        db.delete_table('field_commaseparatedintegerfield')

        # Deleting model 'DateField'
        db.delete_table('field_datefield')

        # Deleting model 'DateTimeField'
        db.delete_table('field_datetimefield')

        # Deleting model 'DecimalField'
        db.delete_table('field_decimalfield')

        # Deleting model 'EmailField'
        db.delete_table('field_emailfield')

        # Deleting model 'FileField'
        db.delete_table('field_filefield')

        # Deleting model 'FilePathField'
        db.delete_table('field_filepathfield')

        # Deleting model 'FloatField'
        db.delete_table('field_floatfield')

        # Deleting model 'ImageField'
        db.delete_table('field_imagefield')

        # Deleting model 'IntegerField'
        db.delete_table('field_integerfield')

        # Deleting model 'IPAddressField'
        db.delete_table('field_ipaddressfield')

        # Deleting model 'NullBooleanField'
        db.delete_table('field_nullbooleanfield')

        # Deleting model 'PositiveIntegerField'
        db.delete_table('field_positiveintegerfield')

        # Deleting model 'PositiveSmallIntegerField'
        db.delete_table('field_positivesmallintegerfield')

        # Deleting model 'SlugField'
        db.delete_table('field_slugfield')

        # Deleting model 'SmallIntegerField'
        db.delete_table('field_smallintegerfield')

        # Deleting model 'TimeField'
        db.delete_table('field_timefield')

        # Deleting model 'URLField'
        db.delete_table('field_urlfield')

        # Deleting model 'XMLField'
        db.delete_table('field_xmlfield')


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

    complete_apps = ['field']