from collections import OrderedDict
from pprint import pprint
import pickle
import xmltodict
from model import LOMModel
from lxml import etree


class Controller:
    _leafs = ['lom:general', 'lom:lifeCycle', 'lom:metaMetadata', 'lom:technical', 'lom:educational',
              'lom:rights', 'lom:relation', 'lom:annotation', 'lom:classification', 'accesibility']

    _mapped_data = dict()
    _object_dict = dict()

    def parse_str_to_dict(self, data: str) -> OrderedDict:
        """
        Parse a valid xml (string) to Python OrderedDict class (Subclass of Dict class).

        :param data: A valid XML string.
        :type data str

        :return: An instance of OrderedDict
        """
        return xmltodict.parse(data)

    def map_recursively(self, dictionary: dict, is_lompad_exported=False):
        """
        Based on an OrderedDict this method map recursively the Dictionary to Python Class.

        :param dictionary: A valid Dict or OrderedDict
        :param is_lompad_exported: Check if manifest comes from lompad application.

        :return: None
        """
        for key, value in dictionary.items():
            if isinstance(dictionary[key], dict):
                if any(key in leaf for leaf in self._leafs) and key != 'lom':
                    self._mapped_data[key], self._object_dict[key] = LOMModel.determine_lompad_leaf(dictionary[key], str(key),
                                                                            is_lompad_exported)
                self.map_recursively(dictionary[key], is_lompad_exported)

    def get_mapped_manifest(self, object_name):
        self.get_object(object_name)
        return self._mapped_data

    def get_mapped_class(self):
        lom_object = LOMModel.LOM()
        for key, value in self._object_dict.items():
            lom_object.__setattr__(key, value)
        return lom_object

    def get_object(self, object_name):
        lom_object = LOMModel.LOM()
        for key, value in self._object_dict.items():
            lom_object.__setattr__(key, value)

        with open('temp_files/'+object_name+'_exported.xml', 'w') as file:
            file.write(lom_object.to_xml().strip())
