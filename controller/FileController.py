import os
from zipfile import ZipFile

import json
from libraries import xmltodict

# Temporal file storage path
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
    Save a file in the specified path.

    param file: The name of the file with its path.
    type: file UploadFile (FastAPI)

    :return: The path of the file created.
    """
    _temporal = get_temp_folder()
    path = _temporal + file.filename
    with open(path, 'wb+') as f:
        f.write(file.file.read())
        f.close()
    return path


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
        xml_dict = xmltodict.parse(ims_manifest_data)
        json_data = json.dumps(xml_dict).replace('\"', '\'')
        return json_data
    except Exception as e:
        print(e)
        return None


"""
    TODO:
        - Remove files after working with them.
    
    DONE:
        - Zip file is deleted after uncompressed.

"""
