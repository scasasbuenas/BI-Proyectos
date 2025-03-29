from proyecto1.parte2.back.Pipeline.Prepipe import Clean, Vectorize, Model
from sklearn.pipeline import Pipeline
from joblib import dump
import pandas as pd
import os


def createPipeline(data):
    # Preparamos la variable objetivo
    y = data['Label']
    X = data.drop(columns=['Label'])

    # Creamos el pipeline
    pipeline = Pipeline([
        ('cleaner', Clean(is_train=True)),
        ('vectorizer', Vectorize(is_train=True)),
        ('model', Model())
    ])

    # Entrenamos el pipeline
    pipeline.fit(X, y)

    # Guardamos el modelo
    os.makedirs('./assets', exist_ok=True)
    dump(pipeline, './assets/model.joblib', compress=True)
    print("[Pipeline] Pipeline guardado en ./assets/model.joblib")


if __name__ == "__main__":
    
    print("¿Existe el  archivo?", os.path.exists('fake_news_spanish.csv'))
    print("[Pipeline] Pipeline Started")
    # Cargar dataset
    df = pd.read_csv('../fake_news_spanish.csv', sep=';', encoding='utf-8')
    # Nos quedamos solo con las columnas relevantes
    df = df[["Label", "Titulo", "Descripcion"]]
    # Aseguramos que todo sea texto
    df["Titulo"] = df["Titulo"].fillna("").astype(str)
    df["Descripcion"] = df["Descripcion"].fillna("").astype(str)
    createPipeline(df)
    print("[Pipeline] Pipeline Finished")
