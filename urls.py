import os

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^field/', include('field.urls')),
    (r'^model/', include('model.urls')),
    (r'^application/', include('application.urls')),
    (r'^project/', include('project.urls')),
    (r'^form/', include('form.urls')),

    (r'^admin/', include(admin.site.urls)),

    url(r'^logout/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout_then_login'),
    (r'^accounts/',
     include('registration.backends.default.urls')),

)

urlpatterns += patterns(
    'django.views.generic.simple',
    (r'^$', 'redirect_to', {'url': '/project/list/'}),
    url(r'^screenshot/$', 'direct_to_template',
        {'template': 'screenshot.html'},
        name='screenshot'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^static/(?P<path>.*)$',
         'django.views.static.serve', {
            'document_root': os.path.join(settings.PROJECT_PATH, 'static/')}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': os.path.join(settings.PROJECT_PATH, 'media/')}),
    )
