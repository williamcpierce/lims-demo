# Generated by Django 4.2.3 on 2023-07-16 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_container_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='inventory.location'),
        ),
    ]
