"""
searchparams module describes properties of the searched user
"""

from typing import List


class BaseField:
    """
    Base fields for properties
    """
    mytype = str

    def __init__(self, name, value, weight=1):
        self.check_type_name(name)
        self.check_type_value(value)
        self.check_type_weight(weight)

        self.name = name
        self.value = value
        self.weight = weight

    @staticmethod
    def check_type_name(name):
        """
        Name is always string. Check if string only
        """
        if isinstance(name, str):
            return name
        raise TypeError('name must be an instance of string')

    @staticmethod
    def check_type_weight(weight):
        """
        Weight is always integer. Check if integer only
        """
        if isinstance(weight, int):
            return weight
        raise TypeError('Weight must be an integer')

    def check_type_value(self, value):
        """
        Value may be a list or a dict. Check the type
        """
        if isinstance(value, self.mytype):
            return value
        raise TypeError('value must be an instance of %s' % type(self.mytype))


class StringField(BaseField):
    """
    Child class for string fields
    """
    mytype = str


class ListField(BaseField):
    """
    Child class for list fields
    """
    mytype = list


class SearchParams:
    """
    Registration of each field of searched params
    """
    def __init__(self, fields: List[BaseField]) -> None:
        self.registry = dict()
        for field in fields:
            self.registry[field.name] = field
