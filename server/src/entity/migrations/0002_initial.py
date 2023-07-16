# Generated by Django 4.2.3 on 2023-07-16 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entity', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='containers',
            field=models.ManyToManyField(blank=True, to='inventory.container'),
        ),
        migrations.AddField(
            model_name='sample',
            name='schema',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='entity.schema'),
        ),
    ]
