# Generated by Django 4.1.5 on 2023-01-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0004_alter_post_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='situation',
            field=models.BooleanField(null=True, verbose_name=False),
        ),
    ]
