# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

{% for model in application.models.all %}{% if model.has_admin_view %}
class {{ model.name }}Admin(admin.ModelAdmin):
    """
    {{ model.name }} admin class
    """
{% if model.admin_list_display.all|length > 0 %}      list_display = ({% for row in model.admin_list_display.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_list_display_links.all|length > 0 %}      list_display_links = ({% for row in model.admin_list_display_links.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_list_filter.all|length > 0 %}      list_filter = ({% for row in model.admin_list_filter.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_list_editable.all|length > 0 %}      list_editable = ({% for row in model.admin_list_editable.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_list_per_page != 100  %}      list_per_page = {{ model.admin_list_per_page }} {% endif %}
{% if model.admin_list_max_show_all != 200 %}      list_max_show_all = {{ model.admin_list_max_show_all }} {% endif %}
{% if model.admin_raw_id_fields.all|length > 0 %}      raw_id_fields = ({% for row in model.admin_raw_id_fields.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_readonly_fields.all|length > 0 %}      readonly_fields = ({% for row in model.admin_readonly_fields.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_filter_horizontal.all|length > 0 %}      filter_horizontal = ({% for row in model.admin_filter_horizontal.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_filter_vertical.all|length > 0 %}      filter_vertical = ({% for row in model.admin_filter_vertical.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_search_fields.all|length > 0 %}      search_fields = ({% for row in model.admin_search_fields.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_ordering.all|length > 0 %}      ordering = ({% for row in model.admin_ordering.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_date_hierarchy %}      date_hierarchy = {{ model.admin_date_hierarchy.object.name }} {% endif %}
{% if not model.admin_actions_selection_counter %}      actions_selection_counter = False{% endif %}
{% if model.admin_exclude.all|length > 0 %}      exclude = ({% for row in model.admin_exclude.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if model.admin_fields.all|length > 0 %}      fields = ({% for row in model.admin_fields.all %}'{{ row.object.name }}',{% endfor %}){% endif %}
{% if not model.admin_has_add_permission %}
      def has_add_permission(self, *args, **kwargs):
          return False
{% endif %}
{% if not model.admin_has_change_permission %}
      def has_change_permission(self, *args, **kwargs):
          return False
{% endif %}
{% if not model.admin_has_delete_permission %}
      def has_delete_permission(self, *args, **kwargs):
          return False
{% endif %}
{%comment%} {% if model.admin_inlines.all|length > 0 %}      inlines = ({% for row in model.admin_inlines.all %}'{{ row.object.name }}',{% endfor %}){% endif %}{%endcomment%}
{% endif %}{% endfor %}


{% for model in application.models.all %}{% if model.has_admin_view %}
admin.site.register({{ model.name }}, {{ model.name }}Admin)
{% endif %}{% endfor %}
