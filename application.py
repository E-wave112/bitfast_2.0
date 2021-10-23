import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List, Dict
from pydantic import BaseModel
from coinbase.wallet.client import Client
from decouple import config
from random import randint
# import the fauna driver
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
# import pytz and datetime to add timestamps to fauna db
from datetime import datetime, date
# import ml model
from ml.model import predict
# import the random identifier
from utils.utils import rand_identifier


fauna_client = FaunaClient(secret=config('FAUNA_SECRET_KEY'))

tags_metadata = [
    {
        "name": "btcprice",
        "description": "Returns the current bitcoin exchange rate in real time for USD and NGN currencies",
    },
    {
        "name": "forecast",
        "description": "Accepts a datetime (in the format YYY-MMM-DDD) object as input and forecasts the bitcoin price(in USD) for that particular date and a fortnight(13 days beyond)."

    },
]
app = FastAPI(

    title="Bitcoin Price predictor",
    description="A Machine learning model built with Python,FastAPI and Fauna that predicts bitcoin prices (in USD and Naira) based on previous market and price data",
    version="1.1.0",
    openapi_tags=tags_metadata
)

# define the coinbase python client
client = Client(config('COINBASE_API_KEY'), config('COINBASE_SECRET_KEY'))


# validate the date format via pydantic
class DateModel(BaseModel):
    date_entered: date


@app.get('/price', tags=['btcprice'])
# function to get current btc prices rates in usd and ngn
async def get_btc():
    rates = client.get_exchange_rates(currency='BTC')
    context = {"usd": rates["rates"]["USD"], "naira": rates["rates"]["NGN"]}
    return {"current bitcoin exchange rates": context}


@app.post('/predict', status_code=200, tags=['forecast'])
# function to forecast current btc prices at a certain time of day
async def forecast(date_input: DateModel, email: Optional[str] = Query('joane@doe.com', min_length=3, max_length=100, regex="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$")):
    date_entered = date_input.date_entered
    prediction_list = predict(date_entered)
    # generate a unique identifier along with the email address a user enters, this is to
    # prevent a unique document error in fauna anytime a user with the same email address tries to forecast a bitcoin app more than once
    u_email_identifier = email + rand_identifier()

    # stores the masked user email into fauna
    try:
        fauna_client.query(
            q.get(q.match(q.index("btcDB"), u_email_identifier)))
    except:
        btc_user = fauna_client.query(q.create(q.collection("btcDB"), {
            "data": {
                "email_address": u_email_identifier,
                "date": datetime.now().strftime('%Y-%m-%d, %H:%m:%S')
            }
        }))
    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")
    response_object = {"email": email,
                       "date entered": date_entered, "forecast": prediction_list}
    return response_object
