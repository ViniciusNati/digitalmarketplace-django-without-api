# Generated by Django 4.1.4 on 2023-01-13 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0050_slugpostsave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sopa', to='aplication.post'),
        ),
    ]