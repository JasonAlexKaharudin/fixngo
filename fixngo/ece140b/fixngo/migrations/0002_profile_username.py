# Generated by Django 2.2.24 on 2021-06-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fixngo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='Orphan', max_length=30),
        ),
    ]
