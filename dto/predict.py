from pydantic import BaseModel
from typing import List


class UnitForecast(BaseModel):
    ds: str
    trend: float


class Predict(BaseModel):
    email: str
    date_entered: str
    forecast: List[UnitForecast]
