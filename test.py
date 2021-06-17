import xmltodict
from model import LOMModel
from collections import OrderedDict

from lxml import objectify
from lxml.etree import fromstring
from lxml import etree


def get_lines(path):
    return ''.join(open(path).readlines())


data = get_lines(
    'C:\\Users\\torre\\Documents\\RESPALDO\\PycharmProjects\\LompadWeb\\temp_files\\'
    'El_sistema_financiero-IMS_CP - IEEE LOM\\imsmanifest_anterior.xml').encode('utf-8')
parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')

data_dict = xmltodict.parse(data)


leafs = ['lomes:general', 'lomes:lifeCycle', 'lomes:metaMetadata', 'lomes:technical', 'lomes:educational',
         'lomes:rights', 'lomes:relation', 'lomes:annotation', 'lomes:classification']


def recursive_function(dictionary):
    for key, value in dictionary.items():
        if isinstance(dictionary[key], dict):
            if any(key in leaf for leaf in leafs):
                LOMModel.determine_lopad_leaf(dictionary[key], key)
            recursive_function(dictionary[key])


recursive_function(data_dict)

dispatch = {
    'lomes:general': 'general_leaf', 'lomes:lifeCycle': 'life_cycle_leaf', 'lomes:metaMetadata': 'meta_metadata_leaf',
    'lomes:technical': 'technical_leaf', 'lomes:educational': 'educational_leaf',
    'lomes:rights': 'rights_leaf', 'lomes:relation': 'relation_leaf', 'lomes:annotation': 'annotation_leaf',
    'lomes:classification': 'classification_leaf'
}