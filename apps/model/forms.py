from django.core.exceptions import ValidationError
from django import forms

from apps.field.models import ModelFieldProxy
from apps.model.utils import slugify
from apps.model.models import Model


class ModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        if 'application' in kwargs:
            self.application = kwargs['application']
            del kwargs['application']

        if 'instance' in kwargs:
            self.application = kwargs['instance'].application

        super(ModelForm, self).__init__(*args, **kwargs)

        self.custom_fields('get_latest_by', kwargs, )
        self.custom_fields('ordering', kwargs)

        self.custom_fields('unique_together', kwargs, True)
        self.custom_fields('index_together', kwargs, True)

        self.custom_fields('admin_list_display', kwargs, True)
        self.custom_fields('admin_list_display_links', kwargs, True)
        self.custom_fields('admin_list_filter', kwargs, True)
        self.custom_fields('admin_list_editable', kwargs, True)
        self.custom_fields('admin_list_per_page', kwargs, True)
        self.custom_fields('admin_list_max_show_all', kwargs, True)
        self.custom_fields('admin_raw_id_fields', kwargs, True)
        self.custom_fields('admin_readonly_fields', kwargs, True)
        self.custom_fields('admin_filter_horizontal', kwargs, True)
        self.custom_fields('admin_filter_vertical', kwargs, True)
        self.custom_fields('admin_search_fields', kwargs, True)
        self.custom_fields('admin_ordering', kwargs, True)
        self.custom_fields('admin_date_hierarchy', kwargs, True)
        self.custom_fields('admin_inlines', kwargs, True)
        self.custom_fields('admin_actions_selection_counter', kwargs, True)
        self.custom_fields('admin_exclude', kwargs, True)
        self.custom_fields('admin_fields', kwargs, True)
        self.custom_fields('admin_has_add_permission', kwargs, True)
        self.custom_fields('admin_has_change_permission', kwargs, True)
        self.custom_fields('admin_has_delete_permission', kwargs, True)

    def custom_fields(self, field, kwargs, multiple=False):
        if field in self.fields:
            if kwargs['instance']:
                self.fields[field].queryset = ModelFieldProxy.objects.filter(
                    model=kwargs['instance'])

                '''
                data = ()
                for obj in ModelField.objects.filter(model=kwargs['instance']):
                    sorting = '%s' % obj.object.name
                    data += ((obj.pk, sorting),)
                    data += (('-%s' % sorting, '-%s' % sorting),)
                data += (('pk', 'pk'),)
                data += (('-pk', '-pk'),)
                if multiple is False:
                    self.fields[field].widget = forms.Select(
                        choices=data
                    )
                else:
                    self.fields[field].widget = forms.SelectMultiple(
                        choices=data
                    )
                '''

    class Meta:
        model = Model
        fields = (
            'name',
            'description',
            'verbose_name',
            'verbose_name_plural',
            'get_latest_by',
            'ordering',
            'unique_together',
            'index_together',
            'managed',
            'is_in_menu',
            'has_read_only_view',
            'has_form_view',
            'has_admin_view',
            'db_table',
            'admin_list_display',
            'admin_list_display_links',
            'admin_list_filter',
            'admin_list_editable',
            'admin_list_per_page',
            'admin_list_max_show_all',
            'admin_raw_id_fields',
            'admin_readonly_fields',
            'admin_filter_horizontal',
            'admin_filter_vertical',
            'admin_search_fields',
            'admin_ordering',
            'admin_date_hierarchy',
            'admin_inlines',
            'admin_actions_selection_counter',
            'admin_exclude',
            'admin_fields',
            'admin_has_add_permission',
            'admin_has_change_permission',
            'admin_has_delete_permission',
        )

    def clean_name(self):
        """
        ensure that a name get cast to CamelCase
        "my model name" should become "MyModelName"
        """
        name = self.cleaned_data["name"]
        name = ''.join(
            ['%s%s' % (x[0].upper(), x[1:]) for x in name.split(' ') if x])
        name = slugify(name)

        if not (self.instance and self.instance.name == name):
            if Model.objects.filter(name=name, application=self.application):
                raise ValidationError(
                    '%s is already in use in this application' % name)

        return name


class NewModelForm(ModelForm):
    class Meta:
        model = Model
        fields = ('name',)
