#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import logging
logger = logging.getLogger(__name__)
import xml.etree.ElementTree as etree

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from .base import Parser


class XMLParser(Parser):
    items_xpath = None

    def parse(self, raw_data):
        tree = etree.parse(raw_data)
        items = tree.findall(self.items_xpath)
        for item in items:
            try:
                item_dict = {}
                for field_name in self.field_names:
                    field = getattr(self, field_name)
                    raw_value = item.find(field.key).text
                    value = field.get_value(raw_value)
                    item_dict[field_name] = value
                yield item_dict
            except (ObjectDoesNotExist, MultipleObjectsReturned) as exc:
                logger.error("Error: {0}".format(exc))



class RSSParser(XMLParser):
    items_xpath = './channel/item'