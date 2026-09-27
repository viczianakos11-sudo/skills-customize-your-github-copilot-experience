from fastapi import FastAPI

app = FastAPI(title="Mergington API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Mergington API!"}


@app.get("/items")
def list_items():
    return [
        {"id": 1, "name": "Sample item"},
        {"id": 2, "name": "Another sample item"},
    ]
