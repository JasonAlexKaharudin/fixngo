# Generated by Django 2.2.24 on 2021-06-04 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fixers', '0002_remove_fixerprofile_is_fixer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FixerProfile',
        ),
    ]