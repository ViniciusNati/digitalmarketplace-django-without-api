# Generated by Django 4.1.4 on 2023-01-13 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0051_alter_comment_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.AddField(
            model_name='comment',
            name='postid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seila', to='aplication.post'),
        ),
    ]