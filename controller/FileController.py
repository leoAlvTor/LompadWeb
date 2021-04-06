import os
from zipfile import ZipFile

import json
from libraries import xmltodict

_temp_files = './temp_files/'


def get_temp_folder():
    if not os.path.exists(_temp_files):
        os.makedirs(_temp_files)
    return _temp_files


def unzip_file(file_path, extraction_path=os.getcwd()+'/temp_files/'):
    with ZipFile(file_path) as file:
        file.extractall(extraction_path)


def delete_temp_file(file_path):
    try:
        os.remove(file_path)
        return True
    except Exception as e:
        print(e)
        return False


def read_ims_manifest(ims_manifest_path):
    with open(ims_manifest_path) as file:
        return ''.join(file.readlines())


def parse_ims_manifest(ims_manifest_data):
    try:
        xml_dict = xmltodict.parse(ims_manifest_data)
        return json.dumps(xml_dict, indent=4)
    except Exception as e:
        print(e)
        return None
