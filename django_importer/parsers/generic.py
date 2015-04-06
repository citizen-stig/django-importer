#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .base import Parser

import xml.etree.ElementTree as etree


class XMLParser(Parser):
    items_xpath = None

    def parse(self, raw_data):
        tree = etree.parse(raw_data)
        items = tree.findall(self.items_xpath)
        for item in items:
            item_dict = {}
            for field_name in self.field_names:
                field = getattr(self, field_name)
                value = field.get_value(item)
                item_dict[field_name] = value
            yield item_dict


class RSSParser(XMLParser):
    items_xpath = './channel/item'