from fastapi import FastAPI, UploadFile, File
from fastapi.exceptions import HTTPException 
from fastapi.responses import FileResponse
import uvicorn
import pandas as pd
from convert import csv_to_json
import os


# D_DIR = r'/home/shady/Downloads'
D_DIR = r'/home/shady/Shady/Week2/Challenge/jsonFiles'
app = FastAPI()

@app.get("/readid")
def read_id():
    return {"hello shady"}

@app.post("/uploadcsv")
def upload_csv(csv_file: UploadFile = File(...)):
    extention = os.path.splitext(csv_file.filename)[-1]
    filename = os.path.splitext(csv_file.filename)[0]
    if extention != ".csv":
        raise HTTPException(400,detail='Invalid document type')
    else:
        df = pd.read_csv(csv_file.file)
        jsonFile, newName = csv_to_json(df, filename)
    SAVE_PATH  = os.path.join(D_DIR,newName)
    # with open(SAVE_PATH,'w') as f:
    return FileResponse(path=SAVE_PATH,media_type="application/json",filename=filename)




if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)
