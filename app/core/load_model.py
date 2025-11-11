import joblib
import os

# 1. Obtener la ruta del directorio del script actual ('app/core/')
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(CURRENT_DIR, '..' , 'models', )

MODEL_LINEAR_FILENAME = 'linear_svc_optimized_model.pkl'
MODEL_VECTORIZER_FILENAME = 'vectorizer.pkl'

MODEL_LINEAR_PATH = os.path.join(MODEL_DIR, MODEL_LINEAR_FILENAME)
MODEL_VECTORIZER_PATH = os.path.join(MODEL_DIR, MODEL_VECTORIZER_FILENAME)

def load_linear_model():
    try:
        model = joblib.load(MODEL_LINEAR_PATH)
        print(f'Modelo linear cargado correctamente desde {MODEL_LINEAR_PATH}')
        return model
    except:
        print(f'Error: No se encontró el modelo linear en la ruta {MODEL_LINEAR_PATH}')
        return None

def load_vectorizer_model():
    try:
        model = joblib.load(MODEL_VECTORIZER_PATH)
        print(f'Modelo Vectorizer cargado correctamente {MODEL_VECTORIZER_PATH}')
        return model
    except:
        print(f'Error: Modelo vectorizer no encontrado en {MODEL_VECTORIZER_PATH}')
        return None
