import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("model.pkl")

# usaremos pydantic para criar classes para instanciar os modelos ML. É uma maneira de representar os dados
class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float


@app.get("/")
def read_root():
    return {"Message": "Fast API is running"}


@app.post("/predict")
def predict(data:InputData):
    input_data = [[data.feature1, data.feature2, data.feature3, data.feature4]]
    prediction = model.predict(input_data)
    return {"prediction": int(prediction)}


# roda usando uvicorn main:app
# em outro terminal roda: curl -X GET "http://127.0.0.1:8000" para receber a mensagem "Fast API is running"
# para fazer um post enviando um conjunto de features e receber uma previsão: curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"feature1":7.2, "feature2":3.5, "feature3":1.4, "feature4":0.2}'