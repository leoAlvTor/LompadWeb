from collections import OrderedDict
from pprint import pprint

import xmltodict
from model import LOMModel
from lxml import etree


class Controller():
    _leafs = ['lomes:general', 'lomes:lifeCycle', 'lomes:metaMetadata', 'lomes:technical', 'lomes:educational',
              'lomes:rights', 'lomes:relation', 'lomes:annotation', 'lomes:classification']

    _mapped_data = dict()

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
        :return: None
        """
        for key, value in dictionary.items():
            if isinstance(dictionary[key], dict):
                if any(key in leaf for leaf in self._leafs) and key != 'lom':
                    self._mapped_data[key] = LOMModel.determine_lompad_leaf(dictionary[key], str(key))
                self.map_recursively(dictionary[key])

    def get_mapped_manifest(self):
        return self._mapped_data
