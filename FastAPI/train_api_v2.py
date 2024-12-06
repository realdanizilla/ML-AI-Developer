import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()



# usaremos pydantic para criar classes para instanciar os modelos ML. É uma maneira de representar os dados
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float


@app.get("/")
def read_root():
    return {"Message": "Fast API is running"}

@app.get("/load_model")
def load_model():
    global model
    model = joblib.load("model.pkl")
    return {"Message": "Model loaded"}

@app.post("/predict")
def predict(data:List[InputData]):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    input_data = [[d.feature1, d.feature2, d.feature3, d.feature4] for d in data]
    try:
        predictions = model.predict(input_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"prediction": predictions.tolist()}

# roda usando uvicorn train_api:app
# posso usar também uvicorn train_api:app --reload para que recarregue caso eu mude o código (somente para ambiente de desenvolvimento)
# em outro terminal roda: curl -X GET "http://127.0.0.1:8000" para receber a mensagem "Fast API is running"
# para fazer um post enviando um conjunto de features e receber uma previsão: curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"feature1":7.2, "feature2":3.5, "feature3":1.4, "feature4":0.2}'