from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name="projects")

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    profile = models.ForeignKey(
        'model.Model', unique=True, blank=True, null=True)

    public = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_public_absolute_url(self):
        if self.public:
            return ('public_project_view', [self.pk])
        return ''

    @models.permalink
    def get_absolute_url(self):
        return ('project_view', [self.pk],)

    class Meta:
        unique_together = (('owner', 'name'),)
