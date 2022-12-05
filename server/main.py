import os

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

from config import SHARED_FILES_FOLDER_NAME

app = FastAPI()


@app.get("/download/{file_name}")
def download_file(file_name: str):
    """
    Download a file from the `files` folder by file_name.

    :param str file_name: name of the file to be returned back to the client
    :return: JSONResponse with an error message if file doesn't exists, otherwise FileResponse
    """

    base_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(base_dir, SHARED_FILES_FOLDER_NAME, file_name)

    if not os.path.exists(file_path):
        return JSONResponse(
            {
                "message": f"File with name {file_name} does not exist "
                           f"in the {SHARED_FILES_FOLDER_NAME} folder."
            }
        )

    return FileResponse(
        path=file_path,
        media_type='application/octet-stream',
        filename=file_name
    )
