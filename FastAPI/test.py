from fastapi.testclient import TestClient
from train_api_v2 import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Fast API is running"}

def test_load_model():
    response = client.get("/load_model")
    assert response.status_code == 200
    assert response.json() == {"Message": "Model loaded"}

def test_predict():
    input_data = [
        {
            "feature1": 5.1,
            "feature2": 3.4,
            "feature3": 1.5,
            "feature4": 0.2,
        },
        {
            "feature1": 6.7,
            "feature2": 3.1,
            "feature3": 4.7,
            "feature4": 1.5,
        }
    ]
    response = client.post("/predict", json=input_data)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert len(response.json()["prediction"]) == 2

# poderia também testar se estamos recebendo o erro com o número que esperamos (Ex: 400 no /predict)
# pensar no camimnho triste, quando algo dá errado