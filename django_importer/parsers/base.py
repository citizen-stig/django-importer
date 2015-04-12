#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class Field:
    """
    Similar to Django Rest Framework field. Holds logic for retrieving value for specific field
    """
    def __init__(self, default=None, key=None):
        self.default = default
        self.key = key
        # These are set up by `.bind()` when the field is added to a serializer.
        self.field_name = None
        self.parent = None

    def bind(self, parent, field_name):
        self.field_name = field_name
        self.parent = parent

    def get_value(self, raw_value):
        return raw_value


class ForeignField(Field):
    """
    Get correct value for Foreign key
    """

    def __init__(self, lookup_field_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lookup_field_name = lookup_field_name

    def get_value(self, *args, **kwargs):
        key_value = super().get_value(*args, **kwargs)
        foreign_model = getattr(self.parent.model, str(self.field_name))
        value = foreign_model.objects.get(**{self.lookup_field_name: key_value})
        return value


class ManyToManyField(Field):
    # TODO: implement this
    pass


class Parser:
    """
    Reads raw data.
    Returns dict for create model kwargs, where:
        - key: model field name
        - value: value for field. Can be model instance for foreignKey

    """
    def __init__(self, model):
        self.model = model
        self.field_names = [x for x in dir(self) if issubclass(getattr(self, x).__class__, Field)]

        for field_name in self.field_names:
            field = getattr(self, field_name)
            field.bind(self, field_name)

    def parse(self, raw_data):
        """
        Main method, which returns
        :param raw_data:
        :return: dictionary or list
        """
        raise NotImplementedError
