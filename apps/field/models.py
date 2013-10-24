from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic
from django.db import models


def docs(key):
    return 'http://docs.djangoproject.com/en/1.4/ref/models/fields/#' + key


class ModelField(models.Model):
    model = models.ForeignKey('model.Model', related_name="model_fields")
    content_type = models.ForeignKey(
        ContentType, verbose_name=_('content type'))
    object_id = models.PositiveIntegerField(_('object id'), db_index=True)
    object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = (('model', 'content_type', 'object_id'),)
        verbose_name = _('model field')
        verbose_name_plural = _('model fields')
        ordering = ('id',)

    def __unicode__(self):
        try:
            return self.object.__unicode__()
        except:
            return unicode(
                'Warning ModelField %d has no object linked to it' % self.pk
            )


class ModelFieldProxy(ModelField):
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.object.name


class Field(models.Model):
    name = models.CharField(max_length=255)
    verbose_name = models.CharField(
        max_length=255, blank=True, help_text=docs('verbose-name'))
    default = models.CharField(
        max_length=255, blank=True, help_text=docs('default'))
    help_text = models.CharField(
        max_length=255, blank=True, help_text=docs('primary-key'))
    null = models.BooleanField(
        default=False, help_text=docs('null'))
    blank = models.BooleanField(default=False, help_text=docs('blank'))
    primary_key = models.BooleanField(
        default=False, help_text=docs('primary-key'))
    unique = models.BooleanField(default=False, help_text=docs('unique'))
    db_index = models.BooleanField(
        default=False, help_text=docs('db-index'))
    editable = models.BooleanField(default=True, help_text=docs('editable'))

    ignored_options = (
        'unicode', 'filefield_ptr', 'datefield_ptr', 'name', 'id')

    class Meta:
        abstract = True

    @property
    def model_field(self):
        field_type = ContentType.objects.get_for_model(self)
        return ModelField.objects.get(
            content_type__pk=field_type.id, object_id=self.id)

    def get_options(self):
        options = []
        for field in self._meta.fields:
            if field.name not in self.ignored_options and (
                self.__getattribute__(field.name)
            ):
                value = self.__getattribute__(field.name)
                if isinstance(value, (unicode, str)):
                    default = value in ('True', 'False') or value.isdigit()
                    if field.name == 'default' and default:
                        option = '%s=%s' % (field.name, value)
                    else:
                        option = '%s=u"%s"' % (
                            field.name, value.replace('"', r'\"'))
                else:
                    option = '%s=%s' % (field.name, value)
                if field.name == 'relation':
                    if value == self.model_field.model:
                        value = 'self'
                    option = "'%s'" % value
                    options.insert(0, option)
                elif field.name == 'choices':
                    choices = ['("%s","%s")' % (
                        choice.strip().replace('"', r'\"'),
                        choice.strip().replace('"', r'\"'))
                        for choice in value.split(',')]
                    options.append('choices=(%s)' % ','.join(choices))
                else:
                    options.append(option)
        return options

    def __unicode__(self):
        return u"%s = models.%s(%s)" % (
            self.name, self.field_type, ', '.join(self.get_options()))


class RelationFieldOption(Field):
    """
    Options that belongs to relation fields
    """
    related_name = models.CharField(
        max_length=255, blank=True,
        help_text=docs('django.db.models.ForeignKey.related_name'))
    relation = models.ForeignKey('model.Model')

    class Meta:
        abstract = True


class OneToOneField(RelationFieldOption):
    form = 'OnoToOneFiedForm'
    field_type = 'OneToOneField'


class ForeignKeyField(RelationFieldOption):
    form = 'ForeignKeyFiedForm'
    field_type = 'ForeignKey'


class ManyToManyField(RelationFieldOption):
    #TODO: see if "through" doesn't make the app more complex
    #through = models.ForeignKey(Model)
    form = 'ManyToManyFieldForm'
    field_type = 'ManyToManyField'


class CharField(Field):
    # indicate if this field will be returned by the the __unicode__ method
    unicode = models.BooleanField(default=False)
    choices = models.TextField(blank=True, help_text=docs('choices'))
    max_length = models.PositiveSmallIntegerField(
        default=255, help_text=docs('django.db.models.CharField.max_length'))
    form = 'CharFieldForm'
    field_type = 'CharField'


class TextField(Field):
    form = 'TextFieldForm'
    field_type = 'TextField'


class AutoField(Field):
    form = 'AutoFieldForm'
    field_type = 'AutoField'


class BigIntegerField(Field):
    form = 'BigIntegerFieldForm'
    field_type = 'BigIntegerField'


class BooleanField(Field):
    form = 'BooleanFieldForm'
    field_type = 'BooleanField'


class CommaSeparatedIntegerField(Field):
    max_length = models.PositiveSmallIntegerField(
        default=255, help_text=docs('django.db.models.CharField.max_length'))
    form = 'CommaSeparatedIntegerFieldForm'
    field_type = 'CommaSeparatedIntegerField'


class DateField(Field):
    auto_now = models.BooleanField(
        default=False, help_text=docs('django.db.models.DateField.auto_now'))
    auto_now_add = models.BooleanField(
        default=False, help_text=docs(
            'django.db.models.DateField.auto_now_add'))
    form = 'DateFieldForm'
    field_type = 'DateField'


class DateTimeField(DateField):
    form = 'DateTimeFieldForm'
    field_type = 'DateTimeField'


class DecimalField(Field):
    max_digits = models.PositiveSmallIntegerField(
        default=5, help_text=docs('django.db.models.DecimalField.max_digits'))
    decimal_places = models.PositiveSmallIntegerField(
        default=2, help_text=docs(
            'django.db.models.DecimalField.decimal_places'))
    form = 'DecimalFieldForm'
    field_type = 'DecimalField'


class EmailField(Field):
    max_length = models.PositiveSmallIntegerField(
        default=75, help_text=docs('django.db.models.CharField.max_length'))
    form = 'EmailFieldForm'
    field_type = 'EmailField'


class FileField(Field):
    max_length = models.PositiveSmallIntegerField(
        default=100, help_text=docs('django.db.models.CharField.max_length'))
    upload_to = models.CharField(
        max_length=255, help_text=docs('django.db.models.FileField.upload_to'))
    form = 'FileFieldForm'
    field_type = 'FileField'


class FilePathField(Field):
    path = models.CharField(
        max_length=255, help_text=docs('django.db.models.FilePathField.path'))
    match = models.CharField(
        max_length=255, help_text=docs('django.db.models.FilePathField.match'))
    recursive = models.BooleanField(
        default=False, help_text=docs(
            'django.db.models.FilePathField.recursive'))
    form = 'FilePathFieldForm'
    field_type = 'FilePathField'


class FloatField(Field):
    form = 'FloatFieldForm'
    field_type = 'FloatField'


class ImageField(FileField):
    height_field = models.CharField(
        max_length=255, blank=True, help_text=docs(
            'django.db.models.ImageField.height_field'))
    width_field = models.CharField(
        max_length=255, blank=True, help_text=docs(
            'django.db.models.ImageField.width_field'))
    form = 'ImageFieldForm'
    field_type = 'ImageField'


class IntegerField(Field):
    form = 'IntegerFieldForm'
    field_type = 'IntegerField'


class IPAddressField(Field):
    form = 'IPAddressFieldForm'
    field_type = 'IPAddressField'


class NullBooleanField(Field):
    form = 'NullBooleanFieldForm'
    field_type = 'NullBooleanField'


class PositiveIntegerField(Field):
    form = 'PositiveIntegerFieldForm'
    field_type = 'PositiveIntegerField'


class PositiveSmallIntegerField(Field):
    form = 'PositiveSmallIntegerFieldForm'
    field_type = 'PositiveSmallIntegerField'


class SlugField(Field):
    max_length = models.PositiveSmallIntegerField(
        default=50, help_text=docs('django.db.models.CharField.max_length'))
    form = 'SlugFieldForm'
    field_type = 'SlugField'


class SmallIntegerField(Field):
    form = 'SmallIntegerFieldForm'
    field_type = 'SmallIntegerField'


class TimeField(DateField):
    form = 'TimeFieldForm'
    field_type = 'TimeField'


class URLField(Field):
    max_length = models.PositiveSmallIntegerField(
        default=200, help_text=docs('django.db.models.CharField.max_length'))
    verify_exists = models.BooleanField(
        default=True, help_text=docs(
            'django.db.models.URLField.verify_exists'))
    form = 'URLFieldForm'
    field_type = 'URLField'


class XMLField(Field):
    schema_path = models.CharField(
        max_length=255, help_text=docs('django.db.models.schema_path'))
    form = 'XMLFieldForm'
    field_type = 'XMLField'
