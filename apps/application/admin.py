from django.contrib import admin
from apps.application.models import Application


class ApplicationAdmin(admin.ModelAdmin):
    search_fields = ('name', 'project')
    list_filter = ('creation_date', 'modification_date')
    list_display = (
        'id', 'name', 'project', 'creation_date', 'modification_date')


admin.site.register(Application, ApplicationAdmin)
