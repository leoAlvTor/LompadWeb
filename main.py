from fastapi import FastAPI, File, UploadFile
from controller import FileController


app = FastAPI()


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    _temporal = FileController.get_temp_folder()

    _filename = _temporal+file.filename

    with open(_filename, 'wb+') as f:
        f.write(file.file.read())
        f.close()
        FileController.unzip_file(_filename)
        FileController.delete_temp_file(_filename)
        # Cambiar el nombre a imsmanifest.xml (Nombre por defecto).
        ims_manifest = FileController.read_ims_manifest(_filename.replace('.zip', '') + '/imsmanifest_anterior.xml')
        ims_manifest = FileController.parse_ims_manifest(ims_manifest)
        print(ims_manifest)

    return {"filename": file.filename}
