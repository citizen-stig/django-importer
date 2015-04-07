#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import http.client
from urllib.parse import urlparse


class Retriever:
    """
    Gets URI
    Returns file like object
    """

    def __init__(self, URI):
        self.URI = URI

    def get_raw_data(self):
        raise NotImplementedError


class HTTPRetriever(Retriever):
    """
    Gets data from HTTP or HTTPS Server
    """
    def __init__(self, URI):
        parsed_url = urlparse(URI)
        if parsed_url.scheme == 'http':
            self.Connection = http.client.HTTPConnection
        elif parsed_url.scheme == 'https':
            self.Connection = http.client.HTTPSConnection
        else:
            raise ValueError("Not supported URL scheme:{0}".format(parsed_url.scheme))
        super().__init__(parsed_url)

    def get_raw_data(self):
        conn = self.Connection(self.URI.netloc)
        conn.request("GET", self.URI.path)
        return conn.getresponse()