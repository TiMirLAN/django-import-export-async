# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 11:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WAITING', 'Waiting'), ('PROCESSED', 'Processed')], default='WAITING', max_length=32)),
                ('export_format', models.PositiveIntegerField()),
                ('report', models.FileField(upload_to='async_reports/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]