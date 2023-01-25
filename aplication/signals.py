"""from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.exceptions import AppRegistryNotReady
   
def ready(self):
    def new_user_callback(sender, instance, created, **kwargs):
        try:
            from aplication.models import Profile
        except AppRegistryNotReady:
            return
        if created:
            Profile.objects.create(user=instance, name=instance.username)
    post_save.connect(new_user_callback, sender=User)"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bank
from django.contrib.auth.models import User
#from . import signals NÃO USE
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Bank.objects.create(user=instance)