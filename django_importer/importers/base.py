#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)

from django.core.exceptions import ValidationError


class BaseImporter:
    """
    Base importer class, which handles model creation
    """
    def __init__(self, model):
        self.model = model

    def import_data(self, address):
        """
        Main method for importing data
        :param address: URI for access data
        :return:
        """
        read_obj = self.get_read_object(address)
        self.parse_data(read_obj)

    def get_read_object(self, address):
        """
        Returns file-like object from given address
        :param address: URI for data
        :return: file-like object
        """
        raise NotImplementedError

    def parse_data(self, source):
        """
        Parses data from sources and calls create_model when data for single model is parsed
        :param source: address of source data. URL or file path
        :return: None
        """
        raise NotImplementedError

    def create_model(self, parsed_data):
        """

        :param parsed_data: dictionary, where:
            - keys are model fields
            - values are a data for that fields. If field is Foreign key or ManyToMany field,
              value should contain only id of relation.
            All exceptions are handled and logged
        :return:
        """
        try:
            self.model.objects.create(**parsed_data)
        except ValidationError as exc:
            logger.error("Error during import model {0}: {1}".format(self.model, exc))
