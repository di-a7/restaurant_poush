# Generated by Django 5.1.6 on 2025-03-07 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0002_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rms.table'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='rms.food'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='rms.order'),
        ),
    ]
