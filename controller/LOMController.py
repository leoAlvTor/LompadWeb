"""
Utilities for IEEE LOM data model
"""

# TESTING
import FileController
import json


def get_elements(json_data):
    import ujson
    ims_manifest = FileController.read_ims_manifest(ims_manifest_path='/home/leo_mx/PycharmProjects/LompadWeb/temp_files/El_sistema_financiero-IMS_CP - IEEE LOM/imsmanifest_nuevo.xml')
    json_ims_manifest = FileController.parse_ims_manifest(ims_manifest)
    iterate_elements(json_ims_manifest)

    ...


def iterate_elements(data_dict):
    ...


get_elements('')
