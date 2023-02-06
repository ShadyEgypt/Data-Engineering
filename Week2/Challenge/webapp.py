from fastapi import FastAPI, UploadFile, File
from fastapi.exceptions import HTTPException 
from fastapi.responses import FileResponse

import pandas as pd
from convert import csv_to_json
from transform import transform
import os


app = FastAPI()

@app.get("/readid")
def read_id():
    return {"hello shady"}

@app.post("/uploadcsv")
def upload_csv(csv_file: UploadFile = File(...)):
    name = csv_file.filename
    extention = os.path.splitext(name)[-1]
    filename = os.path.splitext(name)[0]
    if extention != ".csv":
        raise HTTPException(400,detail='Invalid document type')
    else:
        df = pd.read_csv(csv_file.file)
        newName = csv_to_json(df, filename)
    return FileResponse(newName, media_type="application/json",filename=newName)


@app.post("/transformcsv")
def transform_csv(csv_file: UploadFile = File(...)):
    name = csv_file.filename
    extention = os.path.splitext(name)[-1]
    filename = os.path.splitext(name)[0]
    if extention != ".csv":
        raise HTTPException(400,detail='Invalid document type')
    else:
        df = pd.read_csv(csv_file.file)
        newName = transform(df,name)
    return FileResponse(newName, media_type="application/json",filename=newName)


