from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Message


@receiver(post_save, sender=Message)
def message_post_save(sender, instance, created, **kwargs):
    if created:
        instance.send()
