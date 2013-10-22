from django.db.models.signals import post_delete
from models import ModelField


def delete_linked_field(sender, instance, **kwargs):
    instance.object.delete()


post_delete.connect(delete_linked_field, sender=ModelField)
