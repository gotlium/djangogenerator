# -*- coding: utf-8 -*-

from django.db import models
{% if application.project.profile in application.models.all %}from django.contrib.auth.models import User
from django.db.models.signals import post_save
{% endif %}
{% for model in application.models.all %}
class {{ model.name }}(models.Model):
    {% if model.description %}"""
    {{ model.description }}
    """{% endif %}
    {% for model_field in model.model_fields.all %}
    {{ model_field.object|safe }}{% endfor %}
    {% if project.profile == model %}user = models.OneToOneField(User){% endif %}
{% if model.verbose_name or model.verbose_name_plural or model.get_latest_by or model.managed or model.ordering or model.unique_together.all|length > 1 or model.index_together.all|length > 1 %}
    class Meta:
{% if model.verbose_name %}      verbose_name = u'{{ model.verbose_name }}'{% endif %}
{% if model.verbose_name_plural %}      verbose_name_plural = u'{{ model.verbose_name_plural }}'{% endif %}

{% if model.get_latest_by %}      get_latest_by = '{{ model.get_latest_by.object.name }}'{% endif %}
{% if not model.managed %}      managed = False{% endif %}
{% if model.ordering %}      ordering = ('{{ model.ordering.object.name }}',){% endif %}
{% if model.unique_together.all|length > 1 %}      unique_together = (({% for row in model.unique_together.all %}"{{row.object.name}}",{% endfor %}),){% endif %}
{% if model.index_together.all|length > 1 %}      index_together = (({% for row in model.index_together.all %}"{{row.object.name}}",{% endfor %}),){% endif %}


{% endif %}
{% if model.has_read_only_view or model.has_form_view %}
    @models.permalink
    def get_absolute_url(self):
        {% if  model.has_read_only_view %}return ('{{ model.application.name }}.views.view_{{ model.name.lower }}', [str(self.id)]){% else %}return ('{{ model.application.name}}.views.form_{{ model.name.lower }}', [str(self.id)]){% endif %}

{% endif %}
{% for model_field in model.model_fields.all %}{% if model_field.object.unicode %}
    def __unicode__(self):
        return self.{{ model_field.object.name }}
{% endif %}{% endfor %}{% endfor %}
{% if application.project.profile in application.models.all %}
def create_profile(sender, **kw):
    """
    This method ensure a profile is created with every user creation
    """
    user = kw["instance"]
    if kw["created"]:
        user_profile = {{ application.project.profile.name}}(user=user) # add more property here
        user_profile.save()
post_save.connect(create_profile, sender=User)
{% endif %}
