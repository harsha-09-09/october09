from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import pickle
import pandas as pd
import uvicorn

# Initialize FastAPI app
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Load trained model
with open("california_model.pkl", "rb") as f:
    classifier = pickle.load(f)

# Home page
@app.get("/", response_class=HTMLResponse)
def main_page(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html"
)


# Predict using query parameters
@app.get("/predict")
def predict(
    MedInc: float,
    HouseAge: float,
    AveRooms: float,
    Population: float,
    AveOccup: float,
    Latitude: float
):

    # Create DataFrame with the same feature names
    input_data = pd.DataFrame(
        [[
            MedInc,
            HouseAge,
            AveRooms,
            Population,
            AveOccup,
            Latitude
        ]],
        columns=[
            "MedInc",
            "HouseAge",
            "AveRooms",
            "Population",
            "AveOccup",
            "Latitude"
        ]
    )

    # Make prediction
    prediction = classifier["model"].predict(input_data)

    return {
        "prediction": float(prediction[0])
    }


# Predict using uploaded CSV file
@app.post("/predict_file", response_class=HTMLResponse)
async def predict_file(request: Request, file: UploadFile = File(...)):
    print(f"--> Received file: {file.filename}")
    
    # Read CSV
    df_test = pd.read_csv(file.file)
    print("--> CSV Columns:", df_test.columns.tolist())
    print("--> CSV Shape:", df_test.shape)

    # Run inference
    prediction = classifier['model'].predict(df_test)
    preds_list = [round(float(p), 4) for p in prediction]
    print(f"--> Generated {len(preds_list)} predictions")

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "predictions": preds_list,
            "filename": file.filename
        }
    )

# Run FastAPI server
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )













# from fastapi import FastAPI, UploadFile, File
# import pickle
# import pandas as pd
# import uvicorn  # It is a server to run FastAPI

# # Initialize app
# app = FastAPI()   

# # Load model
# with open("california_model.pkl", "rb") as f:
#     classifier = pickle.load(f)

# @app.get("/")   
# def main_page():
#     return('welcome')
# # Predict from query parameters

# @app.get("/predict")
# def predict(MedInc:float,HouseAge:float,AveRooms:float, 
#            Population:float, AveOccup:float, Latitude:float):
#     input_data = [[MedInc,HouseAge,AveRooms, 
#            Population, AveOccup, Latitude]]
#     prediction = classifier['model'].predict(input_data)
#     return {"prediction": float(prediction[0])}

# # Predict from uploaded CSV file
# @app.post("/predict_file")
# def predict_file(file: UploadFile = File(...)):
#     df_test = pd.read_csv(file.file)
#     prediction = classifier['model'].predict(df_test)
#     return {"predictions": prediction.tolist()}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
