# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('product', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Produtos',
            },
        ),
    ]