# Generated by Django 4.1.5 on 2023-01-09 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0011_comment_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]