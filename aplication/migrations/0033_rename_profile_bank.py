# Generated by Django 4.1.5 on 2023-01-11 12:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplication', '0032_remove_profile_address_remove_profile_birthdate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Bank',
        ),
    ]