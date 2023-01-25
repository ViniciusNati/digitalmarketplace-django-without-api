# Generated by Django 4.1.5 on 2023-01-09 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplication', '0022_profile_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='rg',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='telephone',
        ),
        migrations.CreateModel(
            name='Verified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.IntegerField(null=True)),
                ('rg', models.CharField(max_length=10, null=True)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('birthdate', models.DateField(null=True)),
                ('cep', models.CharField(max_length=8, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('state', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=20, null=True)),
                ('photorg', models.ImageField(upload_to='documents/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]