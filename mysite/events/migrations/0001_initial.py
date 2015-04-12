# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import events.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120, blank=True)),
                ('date', models.CharField(max_length=120)),
            ],
            bases=(events.models.NameRepresentation, models.Model),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
            bases=(events.models.NameRepresentation, models.Model),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
            ],
            bases=(events.models.NameRepresentation, models.Model),
        ),
        migrations.AddField(
            model_name='event',
            name='people',
            field=models.ManyToManyField(to='events.Person', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(to='events.EventType'),
        ),
    ]
