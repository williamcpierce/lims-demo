# Generated by Django 4.2.3 on 2023-07-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eln', '0003_entry_last_modified_by_alter_entry_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Last modified'),
        ),
    ]
