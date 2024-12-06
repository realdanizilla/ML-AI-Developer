import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict

app = FastAPI(
    title="Machine Learning API Test",
    description="This is an API for testing machine learning",
    version="1.0",
    contact={
        "name": "Daniel Ribeiro",
        "url":"http://test.com",
        "email": "daniel@daniel.com"
    }
)



# usaremos pydantic para criar classes para instanciar os modelos ML. É uma maneira de representar os dados
class InputData(BaseModel):
    feature1: float = Field(...,example=5.1, description="Petal size")
    feature2: float = Field(...,example=5.1, description="Petal length")
    feature3: float = Field(...,example=5.1, description="Cepal size")
    feature4: float = Field(...,example=5.1, description="Cepal length")


@app.get("/")
def read_root():
    return {"Message": "Fast API is running"}

@app.get("/load_model")
def load_model():
    global model
    model = joblib.load("model.pkl")
    return {"Message": "Model loaded"}

@app.post("/predict")
def predict(data:List[InputData])-> Dict[str, List[int]]:
    """Endpoint created to classify sets from iris dataset

    Args:
        data (List[InputData]): Input list where inputs are petal size and length and cepal size and length

    Raises:
        HTTPException: Server Error
        HTTPException: _description_

    Returns:
        Dict[str, List[int]]: Dictionary containing the string "predictions" and a List of integers with numbers corresponding to iris categories
    """
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