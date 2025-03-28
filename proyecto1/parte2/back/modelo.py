# Librerías esenciales
import pandas as pd
import numpy as np
import re
import unicodedata
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import SnowballStemmer, WordNetLemmatizer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Descargas necesarias
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Configuración
stopwords_es = set(stopwords.words('spanish'))
stemmer = SnowballStemmer("spanish")
lemmatizer = WordNetLemmatizer()

# Función única de preprocesamiento
def preprocesar_texto(texto):
    texto = str(texto).lower()
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    texto = re.sub(r'[^\w\s]', '', texto)
    palabras = word_tokenize(texto, language="spanish")
    palabras = [p for p in palabras if p not in stopwords_es and not p.isdigit()]
    palabras_stem = [stemmer.stem(p) for p in palabras]
    palabras_lem = [lemmatizer.lemmatize(p, wordnet.VERB) for p in palabras]
    palabras_finales = list(set(palabras_stem + palabras_lem))
    return " ".join(palabras_finales)

# Cargar datos
data = pd.read_csv('proyecto1/parte2/deception/data/fake_news_spanish.csv', sep=';', encoding="utf-8")

data = data[["Label", "Titulo", "Descripcion"]]
data["Texto_Completo"] = data["Titulo"].fillna("") + " " + data["Descripcion"].fillna("")
data["Texto_Completo"] = data["Texto_Completo"].astype(str)

# Aplicar preprocesamiento (ESTA LÍNEA FALTABA)
data["Texto_Procesado"] = data["Texto_Completo"].apply(preprocesar_texto)

# Vectorización
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["Texto_Procesado"])
y = data["Label"]

# Entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train, y_train)

# Predicciones y evaluación con umbral ajustado
y_prob = modelo.predict_proba(X_test)[:, 1]
umbral = 0.6
y_pred = (y_prob >= umbral).astype(int)

print("\nReporte de Clasificación (Umbral 0.6):")
print(classification_report(y_test, y_pred))
print(f"Exactitud del modelo (Umbral 0.6): {accuracy_score(y_test, y_pred):.4f}")

# Prueba con una noticia nueva
noticia_prueba = {
    "Titulo": "La mesa del congreso censura un encuentro internacional de parlamentarios prosáhara en el parlamento",
    "Descripcion": "Portavoces de Ciudadanos, PNV, UPN, PSOE, Unidos PP y EQUO denuncian juntos esta censura que consideran injustificable.",
    "Fecha": "30/10/2018"
}

texto_noticia = noticia_prueba["Titulo"] + " " + noticia_prueba["Descripcion"]
texto_procesado = preprocesar_texto(texto_noticia)
X_nueva = vectorizer.transform([texto_procesado])
pred_nueva = modelo.predict(X_nueva)[0]
prob_nueva = modelo.predict_proba(X_nueva)[0][1]

print("\nResultado de prueba con noticia nueva:")
print(f"Predicción: {'Falsa' if pred_nueva == 1 else 'Verdadera'}")
print(f"Probabilidad de que sea Falsa: {prob_nueva:.4f}")


exit()