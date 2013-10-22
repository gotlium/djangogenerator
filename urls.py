from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^field/', include('apps.field.urls')),
    (r'^model/', include('apps.model.urls')),
    (r'^application/', include('apps.application.urls')),
    (r'^project/', include('apps.project.urls')),
    (r'^form/', include('apps.form.urls')),

    (r'^admin/', include(admin.site.urls)),

    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name='logout_then_login'),
    (r'^accounts/', include('registration.urls')),
)

urlpatterns += patterns(
    'django.views.generic.simple',
    (r'^$', 'redirect_to', {'url': '/project/list/'}),
    url(r'^screenshot/$', 'direct_to_template',
        {'template': 'screenshot.html'},
        name='screenshot'),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
