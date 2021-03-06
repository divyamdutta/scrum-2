# Generated by Django 3.0.7 on 2020-06-09 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20200610_0208'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='logger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='log.Logger'),
        ),
        migrations.AlterField(
            model_name='history',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.Project'),
        ),
        migrations.AlterField(
            model_name='history',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.Team'),
        ),
        migrations.AlterField(
            model_name='history',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
