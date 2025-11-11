from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(title='Regresion API')
app.include_router(router)
