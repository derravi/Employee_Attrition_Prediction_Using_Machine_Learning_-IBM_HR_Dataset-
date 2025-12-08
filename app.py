from fastapi import FastAPI
from Schema.model_pydantic import UserInput
from fastapi.responses import JSONResponse
import pandas as pd
import pickle

#Recive the Models.
with open("Models/model.pkl","rb") as f:
    models = pickle.load(f)

lr = models['linearRegre']
encode = models['encoder']
std = models['standard_scaler']
xgb = models['XGBooster']
temp1 = models['temp1_encode_columns']


app = FastAPI()

@app.get("/")
def default():
    return {"message":"This is the Employee Attrition Prediction",
            "If you want to check the prediction put this into the current url:":"/docs"}

@app.post("/predict")
def prediction(predict:UserInput):
    data = pd.DataFrame([{
    'Age': predict.Age,
    'BusinessTravel': predict.BusinessTravel,
    'DailyRate': predict.DailyRate,
    'Department': predict.Department,
    'DistanceFromHome': predict.DistanceFromHome,
    'Education': predict.Education,
    'EducationField': predict.EducationField,
    'EnvironmentSatisfaction': predict.EnvironmentSatisfaction,
    'Gender': predict.Gender,
    'HourlyRate': predict.HourlyRate,
    'JobInvolvement': predict.JobInvolvement,
    'JobLevel': predict.JobLevel,
    'JobRole': predict.JobRole,
    'JobSatisfaction': predict.JobSatisfaction,
    'MaritalStatus': predict.MaritalStatus,
    'MonthlyIncome': predict.MonthlyIncome,
    'MonthlyRate': predict.MonthlyRate,
    'NumCompaniesWorked': predict.NumCompaniesWorked,
    'OverTime': predict.OverTime,
    'PercentSalaryHike': predict.PercentSalaryHike,
    'PerformanceRating': predict.PerformanceRating,
    'RelationshipSatisfaction': predict.RelationshipSatisfaction,
    'StockOptionLevel': predict.StockOptionLevel,
    'TotalWorkingYears': predict.TotalWorkingYears,
    'TrainingTimesLastYear': predict.TrainingTimesLastYear,
    'WorkLifeBalance': predict.WorkLifeBalance,
    'YearsAtCompany': predict.YearsAtCompany,
    'YearsInCurrentRole': predict.YearsInCurrentRole,
    'YearsSinceLastPromotion': predict.YearsSinceLastPromotion,
    'YearsWithCurrManager': predict.YearsWithCurrManager
    }])

    #Lets encode the all the Labeled Data Columns
    for i in temp1:
        data[i] = encode[i].transform(data[i])
    
    #Lets Scaldown the All the Data
    scaled_data = std.transform(data)

    #Lets use the Linear Regressor model
    lr_predict = lr.predict(scaled_data)
    xgboost_predict = xgb.predict(scaled_data)

    lr_class = int(round(lr_predict[0]))
    xgb_class = int(round(xgboost_predict[0]))

    attrition_encoder = encode['Attrition']

    #Lets invers transform
    lr_final = attrition_encoder.inverse_transform([lr_class])[0]
    xgb_final = attrition_encoder.inverse_transform([xgb_class])[0]

    lr_ans = "Employee is likely to LEAVE the company." if lr_final == "Yes" else "Employee is likely to STAY in the company."
    xgb_ans = "Employee is likely to LEAVE the company." if xgb_final == "Yes" else "Employee is likely to STAY in the company."

    return JSONResponse(
        status_code=200,
        content={
            "The prediction of the Linear Regressor is":lr_ans,
            "The prediction of the XGBoost is":xgb_ans
        })