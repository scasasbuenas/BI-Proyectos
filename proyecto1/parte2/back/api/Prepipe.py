import pandas as pd
import numpy as np
import re
import unicodedata
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords, wordnet
from nltk.stem import SnowballStemmer, WordNetLemmatizer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from scipy.sparse import hstack
from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_score, recall_score, confusion_matrix

class Clean:

    def __init__(self, is_train = False):
        self.stopwords_es = set(stopwords.words('spanish'))
        self.stemmer = SnowballStemmer("spanish")
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer()
        self.news_df = None
        self.tokenizer = RegexpTokenizer(r'\w+')  # This will split on non-word characters

    def remove_non_ascii(self, words):
        """Remueve caracteres no ASCII de una lista de palabras"""
        return [unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore') for word in words if word]

    def to_lower(self, words):
        """Convierte todas las palabras a minúsculas en una lista"""
        return [word.lower() for word in words if word]

    def remove_punctuation(self, words):
        """Elimina signos de puntuación"""
        return [re.sub(r'[^\w\s]', '', word) for word in words if re.sub(r'[^\w\s]', '', word) != '']

    def remove_numbers(self, words):
        """Elimina los números de la lista de palabras"""
        return [word for word in words if not word.isdigit()]
    
    def remove_stopwords(self, words):
        """Elimina stopwords en español"""
        return [word for word in words if word not in self.stopwords_es]
    
    def stem_words(self, words):
        """Aplica stemming para eliminar prefijos y sufijos en las palabras"""
        return [self.stemmer.stem(word) for word in words]
    
    def lemmatize_verbs(self, words):
        """Aplica lematización para obtener la raíz de los verbos"""
        return [self.lemmatizer.lemmatize(word, wordnet.VERB) for word in words]
    
    def stem_and_lemmatize(self, words):
        """Combina stemming y lematización para normalizar los datos"""
        stemmed = self.stem_words(words)
        lemmatized = self.lemmatize_verbs(words)
        return list(set(stemmed + lemmatized))
    
    def preprocessing(self, text):
        """Aplica todas las funciones de limpieza de texto a un string"""
        # Using RegexpTokenizer instead of word_tokenize
        words = self.tokenizer.tokenize(text)
        words = self.remove_non_ascii(words)
        words = self.to_lower(words)
        words = self.remove_numbers(words)
        words = self.remove_stopwords(words)
        words = self.stem_and_lemmatize(words)
        return " ".join(words)
    
    def fit(self, data, target=None):
        self.news_df = data.copy()
        # Unir Título y Descripción en columnas separadas preprocesadas
        self.news_df['Titulo'] = self.news_df['Titulo'].fillna("").astype(str)
        self.news_df['Descripcion'] = self.news_df['Descripcion'].fillna("").astype(str)
        # Aplicar preprocesamiento
        self.news_df['Titulo_Normalizado'] = self.news_df['Titulo'].apply(self.preprocessing)
        self.news_df['Descripcion_Normalizada'] = self.news_df['Descripcion'].apply(self.preprocessing)
        print("[Clean] Fitting terminado. Columnas normalizadas agregadas.")
        return self
    
    def transform(self, data):
        # No modificamos el dataframe original
        df = data.copy()

        # Aseguramos que no haya valores nulos y que sean strings
        df['Titulo'] = df['Titulo'].fillna("").astype(str)
        df['Descripcion'] = df['Descripcion'].fillna("").astype(str)

        # Aplicamos el preprocesamiento
        df['Titulo_Normalizado'] = df['Titulo'].apply(self.preprocessing)
        df['Descripcion_Normalizada'] = df['Descripcion'].apply(self.preprocessing)

        print("[Clean] Transformación terminada. Nuevas columnas agregadas.")
        return df
    
    def predict(self, data):
        return self



class Vectorize:

    def __init__(self, is_train=False):
        self.vectorizer_title = TfidfVectorizer()
        self.vectorizer_description = TfidfVectorizer()
        self.is_train = is_train

    def fit(self, df, target=None):
        # Ajustar los vectorizadores por separado
        self.title_tfidf = self.vectorizer_title.fit_transform(df['Titulo_Normalizado'])
        self.desc_tfidf = self.vectorizer_description.fit_transform(df['Descripcion_Normalizada'])

        # Unir las representaciones
        X = hstack([self.title_tfidf, self.desc_tfidf])
        if self.is_train and target is not None:
            X = X  # Puedes guardar X si lo necesitas
        print("[Vectorize] Fitting terminado. Shape:", X.shape)
        return self

    def transform(self, df):
        # Transformar con los vectorizadores ya ajustados
        title_trans = self.vectorizer_title.transform(df['Titulo_Normalizado'])
        desc_trans = self.vectorizer_description.transform(df['Descripcion_Normalizada'])

        # Concatenar las matrices
        X = hstack([title_trans, desc_trans])
        print("[Vectorize] Transformación terminada. Shape:", X.shape)
        return X




class Model: 

    def __init__(self):
        self.model = LogisticRegression(max_iter=1000)
        self.precision = None
        self.recall = None
        self.report = None
        self.f1 = None
        self.accuracy = None
        self.conf_matrix = None

    def fit(self, data, target):
        # Separar entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(
            data, target, test_size=0.2, random_state=42, stratify=target
        )

        # Entrenamiento del modelo
        self.model.fit(X_train, y_train)

        # Predicciones
        y_pred = self.model.predict(X_test)

        # Métricas
        self.conf_matrix = confusion_matrix(y_test, y_pred)
        self.accuracy = accuracy_score(y_test, y_pred)
        self.report = classification_report(y_test, y_pred)
        self.f1 = f1_score(y_test, y_pred, average='weighted')
        self.recall = recall_score(y_test, y_pred, average='weighted')
        self.precision = precision_score(y_test, y_pred, average='weighted')

        # Reporte
        print(f"[Model] Entrenamiento completado.")
        print(f"[Model] Accuracy: {self.accuracy:.4f}")
        print(f"[Model] F1 Score: {self.f1:.4f}")
        print(f"[Model] Precision: {self.precision:.4f}")
        print(f"[Model] Recall: {self.recall:.4f}")
        print(f"[Model] Classification Report:\n{self.report}")
        return self
    
    def transform(self, data):
        return data

    def predict(self, data):
        # Predice las etiquetas
        labels = self.model.predict(data)

        # Obtiene probabilidades por clase
        probabilities = self.model.predict_proba(data)

        # Construye un DataFrame con las predicciones
        prediction = pd.DataFrame(labels, columns=['label'])

        # Agrega columnas de probabilidades por clase
        for i in range(probabilities.shape[1]):
            prediction[f'prob_class_{i}'] = probabilities[:, i]

        print('predicciones listas')
        return prediction
