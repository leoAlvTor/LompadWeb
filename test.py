import xmltodict
from model import LOMModel


def get_lines(path):
    return ''.join(open(path).readlines())


data = get_lines(
    'C:\\Users\\torre\\Documents\\RESPALDO\\PycharmProjects\\LompadWeb\\temp_files\\'
    'El_sistema_financiero-IMS_CP - IEEE LOM\\imsmanifest_anterior.xml')


data_dict = xmltodict.parse(data)

leafs = ['lomes:general', 'lomes:lifeCycle', 'lomes:metaMetadata', 'lomes:technical', 'lomes:educational',
         'lomes:rights', 'lomes:relation', 'lomes:annotation', 'lomes:classification']


def recursive_function(dictionary, profundidad):
    for key, value in dictionary.items():
        if isinstance(dictionary[key], dict):
            if key in leafs:
                LOMModel.determine_lopad_leaf(dictionary[key], key)
            recursive_function(dictionary[key], profundidad+1)


recursive_function(data_dict, 1)
