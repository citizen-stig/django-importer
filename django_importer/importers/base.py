#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import collections
import logging
logger = logging.getLogger(__name__)

from django.core.exceptions import ValidationError


class BaseImporter:
    """
    Importer users Retriever to get FileLike object with raw data and pass it to the Parser.
    Wher parser returns arguments for models, Importer creates models
    """
    parser = None
    retriever = None
    model = None

    def __init__(self, model=None, parser=None, retriever=None):
        if model:
            self.model = model
        if parser:
            self.parser = parser
        if retriever:
            self.retriever = retriever

    def import_data(self):
        """
        Main method for importing data
        """
        data_obj = self.retriever.get_raw_data()
        parsed_data = self.parser.parse(data_obj)
        if isinstance(parsed_data, collections.Iterable):
            for item in parsed_data:
                self.create_model(item)
        elif isinstance(parsed_data, dict):
            self.create_model(parsed_data)

    def create_model(self, item_data):
        """

        :param item_data: dictionary, where:
            - keys are model fields
            - values are a data for that fields. If field is Foreign key or ManyToMany field,
              value should contain only id of relation.
            All exceptions are handled and logged
        :return:
        """
        try:
            self.model.objects.create(**item_data)
        except ValidationError as exc:
            logger.error("Error during import model {0}: {1}".format(self.model, exc))
