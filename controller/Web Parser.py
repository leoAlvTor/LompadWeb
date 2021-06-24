"""

- El proyecto EXE Learning ya no tiene soporte a nivel de codigo.
- La parte WEB (al exportar como web) no incluye un archivo XML valido con los metadatos necesarios para ser exportados
    a python por lo que este debe ser ignorado.

"""

from collections import OrderedDict

import xmltodict, json
import untangle

# import reflection_test
from model import LOMModel

with open('C:\\Users\\torre\\Documents\\contentv3.xml', 'r') as file:
    content = ''.join(file.readlines())

data = xmltodict.parse(content)

leafs = ['lomes:general', 'lomes:lifeCycle', 'lomes:metaMetadata', 'lomes:technical', 'lomes:educational',
         'lomes:rights', 'lomes:relation', 'lomes:annotation', 'lomes:classification']
ignore_list = ['key', 'uniqueElementName', 'extensiontype_', 'value', 'string', 'size', 'language', 'valueOf_',
                'source', 'exe.engine.lom.lomsubs.roleValueSub', 'exe.engine.lom.lomsubs.sourceValueSub',
                'copyrightAndOtherRestrictions', 'exe.engine.lom.lomsubs.copyrightAndOtherRestrictionsSub',
                'exe.engine.lom.lomsubs.copyrightAndOtherRestrictionsValueSub',
                'creative commons: attribution - share alike', 'LOM-ESv1.0', 'LOMv1.0',
                'exe.engine.lom.lomsubs.LanguageStringSub', 'exe.engine.lom.lomsubs.dateSub', 'dateTime',
               'exe.engine.lom.lomsubs.LangStringSub', 'exe.engine.lom.lomsubs.DateTimeValueSub',
               'exe.engine.lom.lomsubs.VCardSub', 'contribute', 'general', 'lifeCycle', 'metametadata', 'relation',
               'rights', 'technical', 'annotation', 'classification']
values = []


def read_recursive(content):
    for key, value in content.items():
        if isinstance(value, dict):
            read_recursive(value)
        elif isinstance(value, list):
            for dictionary in value:
                if dictionary is not None and isinstance(dictionary, dict):
                    read_recursive(dictionary)
        else:
            if value is not None and value not in ignore_list:
                values.append(value)


read_recursive(data)
lom_dictionary = None #reflection_test.get_lom_dictionary()

values = [value for value in values if value != '']

index_clases = dict()
for index, value in enumerate(values):
    for lom_key in lom_dictionary:
        if str.lower(lom_key+'sub') in str.lower(value):
            if value not in index_clases.keys():
                index_clases[value] = index
            else:
                break

#print(index_clases)
for key, value in index_clases.items():
    print(f"\n************** INICIA {values[value].split('.')[len(values[value].split('.'))-1]} **********************")
    for index in range(value, len(values)):
        print(f'Index: {index} \t Value: {values[index]}')
    print("************** TERMINA **********************")
    print('\n\n')

import json

jason = json.dumps(data, indent=4)
# print(jason)
