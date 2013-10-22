from django import template

from apps.application.forms import ApplicationForm, NewApplicationForm

register = template.Library()


@register.inclusion_tag('application_view.html')
def application_view(application):
    return {'application': application}


@register.inclusion_tag('application_form.html')
def application_form(application):
    app_form = ApplicationForm(
        application.project, instance=application,
        prefix='app_%d_' % application.id)
    return {'application': application, 'application_form': app_form}


@register.inclusion_tag('new_application_form.html')
def new_application_form(project):
    new_app_form = NewApplicationForm(
        project, prefix='new_application_')
    return {'new_application_form': new_app_form, 'project': project}
