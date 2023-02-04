from fastapi import FastAPI

print("This is my docker app")

app = FastAPI()

@app.get("/")
def read_id():
    return {"hello shady"}