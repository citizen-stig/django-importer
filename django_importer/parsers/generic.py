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
                if field.key:
                    raw_value = item.find(field.key).text
                else:
                    raw_value = item.find(field_name).text
                value = field.get_value(raw_value)
                item_dict[field_name] = value
            yield item_dict


class RSSParser(XMLParser):
    items_xpath = './channel/item'