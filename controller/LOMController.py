from collections import OrderedDict

import xmltodict
from model import LOMModel
from lxml import etree


class Controller():

    _leafs = ['lomes:general', 'lomes:lifeCycle', 'lomes:metaMetadata', 'lomes:technical', 'lomes:educational',
         'lomes:rights', 'lomes:relation', 'lomes:annotation', 'lomes:classification']

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