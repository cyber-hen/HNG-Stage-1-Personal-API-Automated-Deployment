from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.get("/health")
def health_check():
    return {"message": "healthy"}

@app.get("/me")
def get_me():
    return {
        "name": " ",
        "email": "your-email@example.com",
        "github": "https://github.com/"
    }
