import json
import xmltodict

def get_lines(path):
    return ''.join(open(path).readlines())


data = get_lines(
    '/home/leo_mx/PycharmProjects/LompadWeb/temp_files/El_sistema_financiero-IMS_CP - IEEE LOM/imsmanifest_anterior.xml')



data_dict = xmltodict.parse(data)
data_json = json.dumps(data_dict, indent=4)
print(data_json)
