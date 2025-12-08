from fastapi import FastAPI
from Schema.model_pydantic import UserInput
import pandas as pd
import pickle

#Recive the Models.
with open("/Models/model.pkl","rb") as f:
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
    dsta = pd.DataFrame({
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
    })
