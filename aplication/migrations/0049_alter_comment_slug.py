# Generated by Django 4.1.4 on 2023-01-13 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0048_alter_comment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
