# Generated by Django 4.1.3 on 2022-11-13 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0013_class_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='students',
        ),
    ]
