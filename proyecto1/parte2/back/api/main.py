from typing import Optional
from DataModel import DataModel
import pandas as pd
from joblib import load
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the absolute path to the model file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "Pipeline", "assets", "model.joblib")

# Model for batch data with correct CSV fields
class BatchDataModel(BaseModel):
    ID: List[str]
    Label: List[int]
    Titulo: List[str]
    Descripcion: List[str]
    Fecha: List[str]

@app.get("/")
def read_root():
   return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/train")
def make_predictions(batch_data: BatchDataModel):
    # Create a DataFrame with features (articles)
    df = pd.DataFrame({
        'Label': batch_data.Label,
        'Titulo': batch_data.Titulo,
        'Descripcion': batch_data.Descripcion,
    })
    
    # Print first row information for each column
    print("First row details:")
    for column in df.columns:
        print(f"{column}: {df[column].iloc[0]}")
        print(f"Type of {column}: {type(df[column].iloc[0])}")
        print("-" * 50)
    
    print(df.sample(10))
    
    y = df['Label']
    X = df.drop(columns=['Label'])
    
    # Load and use the model
    model = load(MODEL_PATH)
    result = model.fit(X, y)
    
    print("\n")
    print("----------------------------------------")
    print("Result:")
    print(result)
    print("----------------------------------------")
    print("\n")
    
    # Get the model component from the pipeline
    model_step = result.named_steps['model']
    
    print(f"Accuracy: {model_step.accuracy}")
    print(f"F1 Score: {model_step.f1}")
    print(f"Precision: {model_step.precision}")
    print(f"Recall: {model_step.recall}")
    print(f"Report: {model_step.report}")
    print(f"Confusion Matrix: {model_step.conf_matrix}")
    

    return (
        float(model_step.accuracy),
        float(model_step.f1),
        float(model_step.precision),
        float(model_step.recall),
        str(model_step.report),
        model_step.conf_matrix.tolist()
    )

@app.post("/predict")
def train(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    
    print("First row details:")
    for column in df.columns:
        print(f"{column}: {df[column].iloc[0]}")
        print(f"Type of {column}: {type(df[column].iloc[0])}")
    
    model = load(MODEL_PATH)
    result = model.predict(df)
    print("Prediction result type:", type(result))
    print("Prediction result:\n", result)
    # Extract the label and convert probabilities to percentages with 2 decimal places
    return (
        int(result['label'].iloc[0]), 
        round(float(result['prob_class_0'].iloc[0] * 100), 2), 
        round(float(result['prob_class_1'].iloc[0] * 100), 2)
    )
