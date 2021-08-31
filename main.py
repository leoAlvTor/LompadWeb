import io
from pprint import pprint

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.openapi.models import Response
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from controller import FileController

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a file from Multipart POST request and return imsmanifest.xml file as JSON.

    :param file: A Multipart Form Data.
    :return:
        imsmanifest.xml as JSON if parse was correct, else raise a new HTTPException with Exception code 500.
    """
    file_type = FileController.get_file_type(file.filename)
    _filepath = None
    _profile = None
    xml_manifest = None
    xml_manifest_ims = -1
    required_tags = ['identifier', 'title', 'language', 'description', 'aggregationLevel', 'metaMetadata',
                     'metadataSchema']

    if file_type == -1:
        return HTTPException(status_code=500, detail='Error, not a valid file type.')
    elif file_type == 1:
        _filepath, _hashed_filename = FileController.save_xml(file)
        xml_manifest = FileController.read_manifest(_filepath)
        if '<lom:lom>' in xml_manifest and all(list([val in xml_manifest for val in required_tags])):
            _profile = 'IMS'
        elif '<lom:lom>' not in xml_manifest and all(list([val in xml_manifest for val in required_tags])):
            _profile = 'SCORM'
    else:
        _filepath, _hashed_filename = FileController.save_zip(file=file)
        FileController.unzip_file(file.filename, _hashed_filename, _filepath)
        FileController.delete_temp_file(_filepath)

        xml_manifest_scorm = FileController.read_manifest(_filepath.replace('.zip', '') + '/imslrm.xml')
        if xml_manifest_scorm == -1:
            xml_manifest_ims = FileController.read_manifest(_filepath.replace('.zip', '') + '/imsmanifest.xml')

        if xml_manifest_ims != -1:
            xml_manifest = xml_manifest_ims
            _profile = 'IMS'
        elif xml_manifest_scorm != -1:
            _profile = 'SCORM'
            xml_manifest = xml_manifest_scorm
        else:
            HTTPException(status_code=500,
                          detail='Error, the uploaded file does not contain imslrm.xml nor imsmanifest.xml files.')

    return {'PERFIL': _profile, 'HASHED_VALUE': _hashed_filename.replace('.zip', '').replace('.xml', '')} \
        if xml_manifest is not None else HTTPException(status_code=500,
                                                       detail='Error trying to parse the'
                                                              ' imsmanifest.xml')


@app.get("/private/read_file/")
async def read_file(hashed_code: str, profile: str):
    from_lompad = False

    if profile == 'SCORM':
        xml_manifest = FileController.read_manifest(f'./temp_files/{hashed_code}/imslrm.xml')
    else:
        xml_manifest = FileController.read_manifest(f'./temp_files/{hashed_code}/imsmanifest.xml')

    if xml_manifest == -1:
        xml_manifest = FileController.read_manifest(f'./temp_files/{hashed_code}.xml')
        from_lompad = True

    if xml_manifest == -1:
        raise HTTPException(status_code=500,
                      detail='Error, file not found or corrupted.')

    if not from_lompad:
        return {'DATA': FileController.load_recursive_model(xml_manifest, hashed_code)}
    else:
        return {'DATA': FileController.load_recursive_model(xml_manifest, hashed_code, is_lompad_exported=True)}


@app.post("/private/update/")
async def update_file(hashed_code: str, hoja, data):
    manifest = FileController.read_manifest(f'./temp_files/{hashed_code}_exported.xml')
    print('PASO 1')
    lom = FileController.load_recursive_as_class(manifest)
    print('PASO 2')
    response = FileController.update_model(hashed_code, hoja, lom, data)
    return {'DATA': response}


@app.get("/private/download/", response_class=FileResponse)
def get_file(hashed_code):
    import glob
    import os

    paths = glob.glob('./temp_files/*')
    for path in paths:
        if hashed_code in path and os.path.isdir(path):
            FileController.write_data(''.join(open(f'./temp_files/{hashed_code}_exported.xml')).strip(),
                                      path.replace('./temp_files\\', ''))
            return FileResponse(path=f'./temp_files/{hashed_code}.zip', filename=f'./temp_files/{hashed_code}.zip')

    import aiofiles
    return FileResponse(path=f'./temp_files/{hashed_code}_exported.xml',
                        filename=f'./temp_files/{hashed_code}_exported.xml')
