#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import http.client
import xml.etree.ElementTree as etree
from urllib.parse import urlparse

from .base import BaseImporter


class RSSImporter(BaseImporter):
    items_xpath = './channel/item'

    def __init__(self, model, item_mapping_dict):
        super().__init__(model)
        self.item_mapping_dict = item_mapping_dict

    def get_read_object(self, address):
        parsed_url = urlparse(address)
        if parsed_url.scheme == 'http':
            conn = http.client.HTTPConnection(parsed_url.netloc)
        elif parsed_url.scheme == 'https':
            conn = http.client.HTTPSConnection(parsed_url.netloc)
        else:
            raise ValueError("Not supported URL scheme:{0}".format(parsed_url.scheme))
        conn.request("GET", parsed_url.path)
        return conn.getresponse()

    def parse_data(self, source):
        tree = etree.parse(source)
        items = tree.findall(self.items_xpath)
        for item in items:
            item_dict = {}
            for key, value in self.item_mapping_dict.items():
                item_dict[key] = item.find(value).text
            self.create_model(item_dict)