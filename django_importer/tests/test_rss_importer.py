#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import unittest

from django_importer.importers.rss import RSSImporter


class Creator:
    def __init__(self, owner):
        self.owner = owner

    def create(self, **kwargs):
        self.owner.put_data(kwargs)


class DummyModel:

    def __init__(self):
        self.data = []
        self.objects = Creator(self)

    def put_data(self, data):
        self.data.append(data)


class RSSImporterTests(unittest.TestCase):

    def test_simple_import(self):
        model = DummyModel()
        mapping = {x: x for x in ('link', 'category', 'pubDate')}
        rss_importer = RSSImporter(model, mapping)
        # TODO: replace with httpretty
        rss_importer.import_data('http://www.feedforall.com/sample.xml')
        print(model.data)
        print(len(model.data))
        self.assertEqual(len(model.data), 9)