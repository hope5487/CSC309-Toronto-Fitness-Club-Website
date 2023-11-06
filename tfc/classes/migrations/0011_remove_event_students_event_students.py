# Generated by Django 4.1.3 on 2022-11-13 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0010_event_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='students',
        ),
        migrations.AddField(
            model_name='event',
            name='students',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
