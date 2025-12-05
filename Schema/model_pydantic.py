from pydantic import BaseModel, Field
from typing import Annotated, Literal

class UserInput(BaseModel):

    Age: Annotated[float, Field(..., description="Enter the Age of the Employee", examples=[35])]
    BusinessTravel: Annotated[str, Field(..., description="Enter the Business Travel type", examples=["Travel_Rarely"])]
    DailyRate: Annotated[float, Field(..., description="Enter the Daily Rate", examples=[800])]
    Department: Annotated[str, Field(..., description="Enter the Department", examples=["Research & Development"])]
    DistanceFromHome: Annotated[float, Field(..., description="Enter the Distance From Home", examples=[5])]
    Education: Annotated[float, Field(..., description="Enter the Education Level (1–5)", examples=[3])]
    EducationField: Annotated[str, Field(..., description="Enter the Education Field", examples=["Life Sciences"])]
    EnvironmentSatisfaction: Annotated[float, Field(..., description="Enter Environment Satisfaction (1–4)", examples=[3])]
    
    Gender: Annotated[str, Field(..., description="Enter Gender", examples=["Male"])]
    
    HourlyRate: Annotated[float, Field(..., description="Enter Hourly Rate", examples=[60])]
    JobInvolvement: Annotated[float, Field(..., description="Enter Job Involvement (1–4)", examples=[3])]
    JobLevel: Annotated[float, Field(..., description="Enter Job Level (1–5)", examples=[2])]
    JobRole: Annotated[str, Field(..., description="Enter Job Role", examples=["Research Scientist"])]
    JobSatisfaction: Annotated[float, Field(..., description="Enter Job Satisfaction (1–4)", examples=[4])]
    
    MaritalStatus: Annotated[str, Field(..., description="Enter Marital Status", examples=["Single"])]
    
    MonthlyIncome: Annotated[float, Field(..., description="Enter Monthly Income", examples=[6500])]
    MonthlyRate: Annotated[float, Field(..., description="Enter Monthly Rate", examples=[20000])]
    NumCompaniesWorked: Annotated[float, Field(..., description="Enter Number of Companies Worked Before", examples=[2])]
    
    OverTime: Annotated[str, Field(..., description="Does Employee Work Overtime? (Yes/No)", examples=["No"])]
    
    PercentSalaryHike: Annotated[float, Field(..., description="Enter Percent Salary Hike", examples=[12])]
    PerformanceRating: Annotated[float, Field(..., description="Enter Performance Rating (1–4)", examples=[3])]
    RelationshipSatisfaction: Annotated[float, Field(..., description="Enter Relationship Satisfaction (1–4)", examples=[3])]
    StockOptionLevel: Annotated[float, Field(..., description="Enter Stock Option Level (0–3)", examples=[1])]
    
    TotalWorkingYears: Annotated[float, Field(..., description="Enter Total Working Years", examples=[8])]
    TrainingTimesLastYear: Annotated[float, Field(..., description="Enter Number of Trainings Last Year", examples=[3])]
    WorkLifeBalance: Annotated[float, Field(..., description="Enter Work Life Balance (1–4)", examples=[3])]
    
    YearsAtCompany: Annotated[float, Field(..., description="Enter Years at Company", examples=[4])]
    YearsInCurrentRole: Annotated[float, Field(..., description="Enter Years in Current Role", examples=[3])]
    YearsSinceLastPromotion: Annotated[float, Field(..., description="Enter Years Since Last Promotion", examples=[1])]
    YearsWithCurrManager: Annotated[float, Field(..., description="Enter Years With Current Manager", examples=[2])]