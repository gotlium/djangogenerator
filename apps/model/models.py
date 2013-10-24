from django.db import models
from apps.model.utils import slugify
from apps.field.models import ModelField


class Model(models.Model):
    name = models.CharField(max_length=255)
    application = models.ForeignKey(
        'application.Application', related_name='models')
    description = models.TextField(blank=True)

    # Meta options
    verbose_name = models.CharField(max_length=255, blank=True)
    verbose_name_plural = models.CharField(max_length=255, blank=True)

    db_table = models.CharField(max_length=255, blank=True)

    get_latest_by = models.ForeignKey(
        ModelField, blank=True, null=True, related_name='latest_by')
    managed = models.BooleanField(default=True)
    ordering = models.ForeignKey(
        ModelField, related_name='order', blank=True, null=True)
    unique_together = models.ManyToManyField(
        ModelField, related_name='uniq', blank=True)
    index_together = models.ManyToManyField(
        ModelField, related_name='index', blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    is_in_menu = models.BooleanField(default=False)
    has_read_only_view = models.BooleanField(default=False)
    has_form_view = models.BooleanField(default=False)
    has_admin_view = models.BooleanField(default=True)

    # Admin options
    admin_list_display = models.ManyToManyField(
        ModelField, related_name='display', blank=True)
    admin_list_display_links = models.ManyToManyField(
        ModelField, related_name='links', blank=True)
    admin_list_filter = models.ManyToManyField(
        ModelField, related_name='filters', blank=True)
    admin_list_editable = models.ManyToManyField(
        ModelField, related_name='editable', blank=True)
    admin_list_per_page = models.IntegerField(default=100)
    admin_list_max_show_all = models.IntegerField(default=200)
    admin_raw_id_fields = models.ManyToManyField(
        ModelField, related_name='raw', blank=True)
    admin_readonly_fields = models.ManyToManyField(
        ModelField, related_name='readonly', blank=True)
    admin_filter_horizontal = models.ManyToManyField(
        ModelField, related_name='horizontal', blank=True)
    admin_filter_vertical = models.ManyToManyField(
        ModelField, related_name='vertical', blank=True)
    admin_search_fields = models.ManyToManyField(
        ModelField, related_name='search', blank=True)
    admin_ordering = models.ForeignKey(
        ModelField, related_name='ordering', blank=True, null=True)
    admin_date_hierarchy = models.ForeignKey(
        ModelField, related_name='date', blank=True, null=True)
    admin_inlines = models.ForeignKey(
        'application.Application', related_name='inline',
        blank=True, null=True)
    admin_actions_selection_counter = models.BooleanField(default=True)
    admin_exclude = models.ManyToManyField(
        ModelField, related_name='exclude', blank=True)
    admin_fields = models.ManyToManyField(
        ModelField, related_name='field', blank=True)
    admin_has_add_permission = models.BooleanField(
        'Admin Has add', default=True)
    admin_has_change_permission = models.BooleanField(
        'Admin Has change', default=True)
    admin_has_delete_permission = models.BooleanField(
        'Admin Has delete', default=True)

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
