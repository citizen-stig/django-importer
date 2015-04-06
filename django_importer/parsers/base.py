#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class Field:
    """
    Similar to Django Rest Framework field
    """
    def __init__(self, default=None):

        self.default = default
        # These are set up by `.bind()` when the field is added to a serializer.
        self.field_name = None
        self.parent = None

    def bind(self, field_name, parent):
        self.field_name = field_name
        self.parent = parent

    def get_value(self, dictionary):
        return dictionary.get(self.field_name, self.default)


class XMLField(Field):

    def get_value(self, xml_item):
        return xml_item.find(self.field_name).text


class ForeignField(Field):

    def __init__(self, lookup_field_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lookup_field_name = lookup_field_name

    def get_value(self, *args, **kwargs):
        key_value = super().get_value(*args, **kwargs)
        foreign_model = getattr(self.parent.model, str(self.field_name))
        value = foreign_model.objects.get(**{self.lookup_field_name: key_value})
        return value


class ForeignXMLField(XMLField, ForeignField):
    pass


class Parser:
    def __init__(self, model):
        self.model = model
        self.field_names = (x for x in dir(self) if issubclass(getattr(self, x).__class__, Field))

        for field_name in self.field_names:
            field = getattr(self, field_name)
            field.bind(self, field_name)

