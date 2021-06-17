import os
from zipfile import ZipFile
from datetime import datetime

import json
from libraries import xmltodict

# Temporal file storage path
from model import LOMModel

_temp_files = './temp_files/'


def get_temp_folder():
    """
    Create a new temporal folder for data storage.

    :return:
        _temp_files represents the temporal folder.

    """
    if not os.path.exists(_temp_files):
        os.makedirs(_temp_files)
    return _temp_files


def save_file(file):
    """
    Save a file in the specified path using hash values, by this avoid overwrite by users.

    param file: The name of the file with its path.
    type: file UploadFile (FastAPI)

    :return: The path of the file created.
    """
    _temporal = get_temp_folder()
    hashed_filename = file.filename + "_" + str(hash(file.filename+datetime.today().strftime('%Y-%m-%d-%H:%M:%S')))
    path = _temporal + hashed_filename
    with open(path, 'wb+') as f:
        f.write(file.file.read())
        f.close()
    return path, hashed_filename


def unzip_file(file_path, extraction_path=os.getcwd()+'/temp_files/'):
    """
    Uncompress a zip file.

    param file_path: The path of the zip file.
    type file_path str

    param extraction_path: The path of extraction, by default it's inside temporal folder.
    type extraction_path str

    :return:
        None
    """

    with ZipFile(file_path) as file:
        file.extractall(extraction_path)


def delete_temp_file(file_path):
    """
    Try to delete a temporal file.

    param file_path: The location of the file with its name.
    type file_path str

    :return:
        True if file was deleted or False if an error occurred.
    """
    try:
        os.remove(file_path)
        return True
    except Exception as e:
        print(e)
        return False


def read_ims_manifest(ims_manifest_path):
    """
    Read the ims_manifest XML file by its path.

    param ims_manifest_path: The path of the ims_manifest XML.
    type ims_manifest_path str

    :return:
        A string representing the whole file.
    """
    with open(ims_manifest_path) as file:
        return ''.join(file.readlines())


def parse_ims_manifest(ims_manifest_data):
    """
    Parse a valid XML string to JSON.

    param ims_manifest_data: An XML string with ims_manifest data.
    type ims_manifest_data str

    :return:
        A valid JSON if parsing process was correct, else None.
    """
    try:
        return xmltodict.parse(ims_manifest_data)
    except Exception as e:
        print(e)
        return None


def load_recursive_model(ims_manifest_data):
    """
    Load LOMPAD XML file into Python Class

    :param ims_manifest_data:
    :return:
    """

    data_dict = xmltodict.parse(ims_manifest_data)
    leafs = ['lomes:general', 'lomes:lifeCycle', 'lomes:metaMetadata', 'lomes:technical', 'lomes:educational',
             'lomes:rights', 'lomes:relation', 'lomes:annotation', 'lomes:classification']

    def recursive_function(dictionary):
        print(dictionary)
        for key, value in dictionary.items():
            if isinstance(dictionary[key], dict):
                if key in leafs:
                    LOMModel.determine_lopad_leaf(dictionary[key], key)
                recursive_function(dictionary[key])
    recursive_function(data_dict)


"""
    TODO:
        - Remove files after working with them.
    
    DONE:
        - Zip file is deleted after uncompressed.

"""
