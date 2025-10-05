from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from django.dispatch import receiver

from .models import Project


@receiver(m2m_changed, sender=Project.linked_projects.through)
def prevent_self_link(sender, instance, action, pk_set, **kwargs):
    if action == "pre_add":
        if instance.pk in pk_set:
            raise ValidationError("A project cannot be linked to itself.")
