#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import collections
import logging
logger = logging.getLogger(__name__)

from django.core.exceptions import ValidationError


class BaseImporter:
    """
    Importer users Retriever to get FileLike object with raw data and pass it to the Parser.
    When parser returns arguments for models, Importer creates models
    """
    parser_class = None
    retriever = None
    model = None

    def __init__(self, model=None, parser_class=None, retriever=None):
        if model:
            self.model = model
        if parser_class:
            self.parser_class = parser_class
        self.parser = self.parser_class(self.model)
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
            logger.error("Error during import model: {0}".format(exc))
