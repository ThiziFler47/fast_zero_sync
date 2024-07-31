from fastapi import FastAPI

app = FastApi()

@app.get('/')
def read_root():
    return {"message": "Olá Mundis!"}
