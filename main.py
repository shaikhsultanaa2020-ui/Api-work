from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Running"}

@app.get("/api/v1/health")
def health():
    return {"status": "ok"}
