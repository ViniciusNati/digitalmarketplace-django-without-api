# Generated by Django 4.1.5 on 2023-01-09 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0008_post_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='amountselled',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
