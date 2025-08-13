from fastapi import FastAPI
from src.api import main_router
import uvicorn

app = FastAPI()
app.include_router(main_router)

#uvicorn src.main:app --reload

# Initiate app: python main.py
# if __name__ == "__main__":
#     uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)