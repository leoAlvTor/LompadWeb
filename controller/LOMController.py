from collections import OrderedDict

import xmltodict
from model import LOMModel
from lxml import etree


class Controller():

    _leafs = ['lomes:general', 'lomes:lifeCycle', 'lomes:metaMetadata', 'lomes:technical', 'lomes:educational',
         'lomes:rights', 'lomes:relation', 'lomes:annotation', 'lomes:classification']

    def parse_str_to_dict(self, data: str) -> OrderedDict:
        """
        Parse a valid xml (string) to Python OrderedDict class (Subclass of Dict class).

        :param data: A valid XML string.
        :type data str

        :return: An instance of OrderedDict
        """
        return xmltodict.parse(data)

    def map_recursively(self, dictionary: dict):
        """
        Based on an OrderedDict this method map recursively the Dictionary to Python Class.

        :param dictionary: A valid Dict or OrderedDict
        :return: None (Under development).
        """
        for key, value in dictionary.items():
            if isinstance(dictionary[key], dict):
                if any(key in leaf for leaf in self._leafs):
                    LOMModel.determine_lopad_leaf(dictionary[key], key)
                self.map_recursively(dictionary[key])
