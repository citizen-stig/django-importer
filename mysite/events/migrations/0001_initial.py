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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120, blank=True)),
                ('date', models.DateField()),
            ],
            bases=(events.models.NameRepresentation, models.Model),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=120)),
            ],
            bases=(events.models.NameRepresentation, models.Model),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
            ],
            bases=(events.models.NameRepresentation, models.Model),
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ManyToManyField(to='events.Place'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(to='events.EventType'),
        ),
    ]
