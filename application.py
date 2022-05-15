import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List, Dict
from pydantic import BaseModel
from decouple import config

# import the fauna driver
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

# import pytz and datetime to add timestamps to fauna db
from datetime import datetime, date

# import ml model
from ml.model import predict

# import the random identifier
from utils.rand_utils import rand_identifier

# import crypto utils
from utils.crypto_utils import get_crypto_prices

#import dtos
from dto.predict import Predict
from dto.metadata import MetaData

fauna_client = FaunaClient(secret=config("FAUNA_SECRET_KEY"))

tags_metadata: List[MetaData] = [
    {"name": "getting-started", "description": "A primer into bitfast!"},
    {
        "name": "btcprice",
        "description": "Returns the current bitcoin exchange rate in real time for USD and NGN currencies",
    },
    {
        "name": "forecast",
        "description": "Accepts a datetime (in the format YYY-MMM-DDD) object as input and forecasts the bitcoin price(in USD) for that particular date and a fortnight(13 days beyond).",
    },
]
app = FastAPI(
    title="Bitcoin Price predictor",
    description="A Machine learning model built with Python,FastAPI and Fauna that predicts bitcoin prices (in USD and Naira) based on previous market and price data",
    version="1.1.0",
    openapi_tags=tags_metadata,
)



class DateModel(BaseModel):
    date_entered: date


@app.get("/", tags=["getting-started"])
async def index() -> str:
    return "welcome to bitfast!, kindly access this url https://bitfast.herokuapp.com/docs to fully explore the API"


@app.get("/price", tags=["btcprice"])
async def get_btc():
    return get_crypto_prices()


@app.post("/predict", status_code=200, tags=["forecast"])
# function to forecast current btc prices at a certain time of day
async def forecast(
    date_input: DateModel,
    email: Optional[str] = Query(
        "joane@doe.com",
        min_length=3,
        max_length=100,
        regex="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$",
    ),
) -> Predict:
    date_entered = date_input.date_entered
    prediction_list = predict(date_entered)
    # generate a unique identifier along with the email address a user enters, this is to
    # prevent a unique document error in fauna anytime a user with the same email address tries to forecast a bitcoin app more than once
    u_email_identifier = email + rand_identifier()

    # stores the masked user email into fauna
    try:
        fauna_client.query(q.get(q.match(q.index("btcDB"), u_email_identifier)))
    except:
        btc_user = fauna_client.query(
            q.create(
                q.collection("btcDB"),
                {
                    "data": {
                        "email_address": u_email_identifier,
                        "date": datetime.now().strftime("%Y-%m-%d, %H:%m:%S"),
                    }
                },
            )
        )
    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")
    response_object = {
        "email": email,
        "date entered": date_entered,
        "forecast": prediction_list,
    }
    return response_object
