# Generated by Django 4.1.5 on 2023-01-09 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0007_post_premium'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
