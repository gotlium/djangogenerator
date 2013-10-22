from django.contrib import admin
from apps.field import models

for mem in dir(models):
    if not mem.startswith('Field') and mem.endswith('Field'):
        admin.site.register(getattr(models, mem))
