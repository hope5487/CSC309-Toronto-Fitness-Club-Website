# Generated by Django 4.1.2 on 2022-10-27 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('swift_code', models.CharField(max_length=200)),
                ('institution_number', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('transit_number', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(default='admin@utoronto.ca', max_length=254)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='banks.bank')),
            ],
        ),
    ]
