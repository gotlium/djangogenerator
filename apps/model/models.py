from django.db import models

from apps.model.utils import slugify


class Model(models.Model):
    name = models.CharField(max_length=255)
    application = models.ForeignKey('application.Application',
                                    related_name='models')
    description = models.TextField(blank=True)

    # Meta options
    verbose_name = models.CharField(max_length=255, blank=True)
    verbose_name_plural = models.CharField(max_length=255, blank=True)
    #TODO: need to be clarified
    #app_label = models.CharField(max_length=255, blank=True)
    db_table = models.CharField(max_length=255, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    is_in_menu = models.BooleanField(default=False)
    has_read_only_view = models.BooleanField(default=False)
    has_form_view = models.BooleanField(default=False)
    has_admin_view = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s.%s" % (self.application, self.name)

    def unicode_field(self):
        unicodes = self.model_fields.filter(object__unicode=True)
        return unicodes and unicodes[0] or False


class Permissions(models.Model):
    model = models.ForeignKey(Model, related_name="permissions")
    name = models.CharField(max_length=55)

    def __unicode__(self):
        return '("%s", "%s")' % (slugify(self.name), self.name)

