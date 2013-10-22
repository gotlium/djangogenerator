from django.contrib import admin
from apps.model.models import Model


class ModelAdmin(admin.ModelAdmin):
    """
    Model admin page
    """
    search_fields = ('name', 'application')
    list_filter = ('creation_date', 'modification_date')
    list_display = (
        'id', 'name', 'application', 'creation_date', 'modification_date')


admin.site.register(Model, ModelAdmin)
