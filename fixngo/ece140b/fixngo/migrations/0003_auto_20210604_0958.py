# Generated by Django 2.2.24 on 2021-06-04 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fixngo', '0002_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='s_RepairRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Date Created')),
                ('is_taken', models.BooleanField(default=False, null=True)),
                ('operating_system', models.CharField(choices=[('MacOS', 'MacOS'), ('windows', 'Windows'), ('linux', 'Linux')], default='windows', max_length=15)),
                ('customer_postalCode', models.IntegerField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Software Repair Request',
                'verbose_name_plural': 'Software Repair Requests',
            },
        ),
        migrations.CreateModel(
            name='h_RepairRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repair_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('device', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='Date Created')),
                ('is_taken', models.BooleanField(default=False, null=True)),
                ('customer_postalCode', models.IntegerField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hardware Repair Request',
                'verbose_name_plural': 'Hardware Repair Requests',
            },
        ),
    ]
