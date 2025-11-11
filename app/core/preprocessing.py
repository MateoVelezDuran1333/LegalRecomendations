import re
import string
import nltk
from nltk.corpus import stopwords
from ..core.load_model import load_vectorizer_model
#nltk.download('stopwords')
#stop_words = set(stopwords.words('english'))
import spacy
# !python -m spacy download en_core_web_sm
#nlp_en = spacy.load('en_core_web_sm')


class Preprocesamiento():
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.nlp_en = spacy.load('en_core_web_sm')
        self.model_vectorizer = load_vectorizer_model()


    def clean_text(self, text: str) -> str:
        """
        Función de limpieza de texto que combina la robustez web con la eliminación
        de ruido específico de documentos legales (citas, números de caso).
        """
        # 1. Convertir a minúsculas
        text = str(text).lower()

        # 2. Eliminar texto entre corchetes (etiquetas tipo [duplicate] o referencias legales)
        text = re.sub(r'\[.*?\]', '', text)

        # 3. Eliminar URLs
        text = re.sub(r'https?://\S+|www\.\S+', '', text)

        # 4. Eliminar etiquetas HTML
        text = re.sub(r'<.*?>+', '', text)

        # 5. ELIMINAR RUIDO LEGAL Y NUMÉRICO:
        #    - Elimina números (años, volúmenes, páginas)
        #    - Elimina paréntesis y punto y coma (estructuras típicas de cita)
        text = re.sub(r'[0-9]+|;|\(|\)', '', text)

        # 6. Eliminar puntuación, pero conservar signos útiles (ej: '?')
        punctuation = string.punctuation.replace('?', '')
        text = re.sub(r'[%s]' % re.escape(punctuation), '', text)

        # 7. Eliminar saltos de línea y tabulaciones
        text = re.sub(r'\n|\t', ' ', text)

        # 8. Eliminar caracteres no ASCII (emojis, símbolos raros)
        text = re.sub(r'[^\x00-\x7F]+', '', text)

        # 9. Eliminar espacios extra y recortar
        text = re.sub(r'\s+', ' ', text).strip()

        return text

    def clean_lemmatized_delete_stopwords(self, txt : str) -> str:
        clean_data = self.clean_text(txt)
        doc_en = self.nlp_en(clean_data)
        lemmatized = [token.lemma_ for token in doc_en if token.text.lower() not in self.stop_words]
        return ' '.join(lemmatized).strip()
    
    def vectorizer(self, txt : str):
        data = self.model_vectorizer.transform([txt])
        return data
    
    def processing_data(self, txt : str):
        txt = self.clean_lemmatized_delete_stopwords(txt)
        vectorized = self.vectorizer(txt)
        return vectorized