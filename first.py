from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API chal rahi hai"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/sub")
def sub(a: float, b: float):
    return {"result": a - b}

@app.get("/mul")
def mul(a: float, b: float):
    return {"result": a * b}

@app.get("/div")
def div(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": a / b}