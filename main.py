from fastapi import FastAPI
import uvicorn
from controllers.companies_controller import *

app = FastAPI()

# Initiate app: python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)