from FastAPI import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World!"


# roda usando uvicorn main:app
# em outro terminal roda "curl URL_DO_SERVIDOR_COM_PORTA"