from fastapi import FastAPI, File, UploadFile, HTTPException
from starlette.middleware.cors import CORSMiddleware

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
    _filename = FileController.save_file(file=file)
    FileController.unzip_file(_filename)
    FileController.delete_temp_file(_filename)
    # Cambiar el nombre a imsmanifest.xml (Nombre por defecto).
    ims_manifest = FileController.read_ims_manifest(_filename.replace('.zip', '') + '/imsmanifest_nuevo.xml')
    ims_manifest = FileController.parse_ims_manifest(ims_manifest)

    return ims_manifest if ims_manifest is not None else HTTPException(status_code=500,
                                                                       detail='Error trying to parse the'
                                                                              ' imsmanifest.xml')
