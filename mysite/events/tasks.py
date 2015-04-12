#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django_importer.parsers.generic import RSSParser
from django_importer.parsers.base import Field, ForeignField, ManyToManyField
from django_importer.retrievers.base import HTTPRetriever
from django_importer.importers.base import BaseImporter


from . import models


class EventParser(RSSParser):
    name = Field(key='title')
    description = Field()
    date = Field(key='pubDate')
    type = ForeignField(key='category', lookup_field_name='name')


class EventImporter(BaseImporter):
    model = models.Event
    retriever = HTTPRetriever('http://www.feedforall.com/sample.xml')
    parser_class = EventParser
