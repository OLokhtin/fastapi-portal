from fastapi import FastAPI
from src.api import main_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.include_router(main_router)
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:63342"])

# uvicorn src.main:app --reload
# python -m src.main
if __name__ == "__main__":
     uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)