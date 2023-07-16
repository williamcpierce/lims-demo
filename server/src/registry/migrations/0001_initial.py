# Generated by Django 4.2.3 on 2023-07-16 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('prefix', models.CharField(max_length=3, unique=True)),
                ('digits', models.IntegerField(verbose_name='ID Digits')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField(blank=True, null=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('containers', models.ManyToManyField(blank=True, to='inventory.container')),
                ('schema', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='registry.schema')),
            ],
        ),
    ]