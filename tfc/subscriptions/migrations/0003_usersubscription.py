# Generated by Django 4.1.3 on 2022-11-11 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0002_subcriptionplan_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.PositiveIntegerField()),
                ('cvv', models.PositiveIntegerField()),
                ('expiry', models.PositiveIntegerField(help_text='Enter as MMYY')),
                ('renew', models.BooleanField()),
                ('last_paid', models.DateField(auto_now_add=True)),
                ('curr_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='subscriptions.subcriptionplan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
