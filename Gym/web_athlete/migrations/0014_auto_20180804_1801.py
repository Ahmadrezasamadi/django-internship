# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-04 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_athlete', '0013_auto_20180804_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class_times',
            old_name='open_t',
            new_name='Open_times',
        ),
        migrations.AlterField(
            model_name='class_times',
            name='Open_times',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_athlete.Time_option'),
        ),
        migrations.AlterField(
            model_name='fields',
            name='class_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_athlete.Class_times'),
        ),
        migrations.AlterField(
            model_name='member',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_athlete.Fields'),
        ),
    ]
