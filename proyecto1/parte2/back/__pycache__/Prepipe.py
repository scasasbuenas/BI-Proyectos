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
from scipy.sparse import hstack

class Clean:

    def __init__(self, is_train = False):
        self.stopwords_es = set(stopwords.words('spanish'))
        self.stemmer = SnowballStemmer("spanish")
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = TfidfVectorizer()
        self.news_df = None


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
        words = word_tokenize(text, language="spanish")  # Tokenizar con NLTK
        words = self.remove_non_ascii(words)
        words = self.to_lower(words)
        words = self.remove_punctuation(words)
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
