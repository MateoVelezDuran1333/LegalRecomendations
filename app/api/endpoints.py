from fastapi import APIRouter, HTTPException
from .schemas import Item, combine_title_and_text
from ..core.load_model import load_linear_model
from ..core.preprocessing import Preprocesamiento


router = APIRouter()
linear_model = load_linear_model()
preprocesamiento = Preprocesamiento()

map_outcome = {
    'cited': 1,
    'referred to': 2,
    'applied': 3,
    'followed': 4,
    'considered': 5,
    'discussed': 6,
    'distinguished': 7,
    'related': 8,
    'affirmed': 9,
    'approved': 10
}

# Invertimos el diccionario para decodificar las salidas del modelo
decode_outcome = {v: k for k, v in map_outcome.items()}

@router.post('/prediction')
async def prediction(item : Item) -> dict:
    if linear_model is None:
        raise HTTPException(status_code=500, detail="Modelo lineal no cargado correctamente")
    txt = combine_title_and_text(item)
    vectorized_txt = preprocesamiento.processing_data(txt)
    pred = linear_model.predict(vectorized_txt)
    pred_num = int(pred[0])
    pred_label = decode_outcome.get(pred_num, "Unknown")
    return {
        "prediction_code": pred_num,
        "prediction_label": pred_label
    }

