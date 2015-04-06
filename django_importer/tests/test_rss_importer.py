#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import unittest

from django_importer.parsers.generic import RSSParser
from django_importer.parsers.base import Field, XMLField
from django_importer.retrievers.base import HTTPRetriver
from django_importer.importers.base import BaseImporter



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

        class Parser(RSSParser):
            link = XMLField('link')
            category = XMLField('category')
            pub_data = XMLField('pubDate')

        parser = Parser(model)
        retriever = HTTPRetriver('http://www.feedforall.com/sample.xml')

        importer = BaseImporter(model=model, parser=parser, retriever=retriever)

        # TODO: replace with httpretty
        importer.import_data()
        print(model.data)
        print(len(model.data))
        self.assertEqual(len(model.data), 9)