from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def default():
    return {"message":"This is the Employee Attrition Prediction",
            "If you want to check the prediction put this into the current url:":"/docs"}
@app.get()