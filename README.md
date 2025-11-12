# ⚖️ Legal Recomendations - NLP Regression API

**Legal Recomendations** es una API basada en **FastAPI** que utiliza modelos de **Machine Learning (NLP)** para analizar textos legales y predecir la relación entre documentos jurídicos (por ejemplo, si un fallo fue *citado*, *referido*, *aplicado*, etc.).  

Este proyecto incluye un pipeline completo de preprocesamiento, vectorización y predicción, todo empaquetado en un contenedor **Docker** y desplegado en la nube mediante **Render**.

---

## 🚀 Tecnologías utilizadas

- **FastAPI** – Framework para construir APIs rápidas y modernas.  
- **spaCy** – Procesamiento del lenguaje natural (lemmatización).  
- **NLTK** – Manejo de *stopwords* en inglés.  
- **scikit-learn** – Modelo lineal y vectorizador TF-IDF.  
- **Docker** – Contenerización del proyecto.  
- **Render** – Despliegue en la nube.  

---

## 🧠 Estructura del proyecto
```bash
app/
│
├── api/
│ ├── endpoints.py # Rutas de la API
│ └── schemas.py # Esquemas Pydantic
│
├── core/
│ ├── load_model.py # Carga de modelos serializados
│ ├── preprocessing.py # Limpieza y lematización
│ └── ../models/ # Archivos .pkl del modelo y vectorizador
│
├── main.py # Punto de entrada de FastAPI
├── requirements.txt # Dependencias del proyecto
└── Dockerfile # Configuración de imagen Docker
```

---

## ⚙️ Instalación local

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/MateoVelezDuran1333/LegalRecomendations.git
cd LegalRecomendations
```

### 2️⃣ Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows

pip install -r requirements.txt
```
### 3️⃣ Descargar modelos adicionales
```bash
python -m spacy download en_core_web_sm
python -m nltk.downloader stopwords
```
### 4️⃣ Ejecutar el servidor localmente
```bash
uvicorn app.main:app --reload
```
La API estará disponible en 👉 http://127.0.0.1:8000/docs

## 🧩 Endpoint principal
Ejemplo de petición
```bash
curl -X POST "https://legalrecomendations.onrender.com/prediction" \
-H "Content-Type: application/json" \
-d '{"title": "Court decision about contract", "text": "The court applied previous similar cases to determine the outcome."}'
```
Ejemplo de respuesta
```bash
{
  "prediction_code": 2,
  "prediction_label": "referred to"
}
```

## 🐳 Uso con Docker
### 1️⃣ Construir la imagen
```bash
docker build -t regresion-api .
```
### 2️⃣ Ejecutar el contenedor
```bash
docker run -d -p 8000:8000 regresion-api
```
Luego accede a: http://localhost:8000/docs

## 🧾 Licencia

Este proyecto fue desarrollado con fines académicos como parte de un proyecto de Ingeniería de Sistemas, enfocado en la aplicación de técnicas de Procesamiento de Lenguaje Natural (NLP) y aprendizaje automático para el análisis jurídico.
