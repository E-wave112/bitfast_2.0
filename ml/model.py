from prophet import Prophet
import datetime
import sys
import warnings
import boto3
import pandas as pd
from decouple import config

from utils.constants import AWS_BUCKET_NAME, FORECAST_INTERVAL, OBJECT_KEY

warnings.filterwarnings("ignore")


def train(model="bitcoin"):
    if sys.version_info[0] < 3:
        from StringIO import StringIO  # Python 2.x
    else:
        from io import StringIO  # Python 3.x
    # set your credentials and secret
    AWS_ID = config("AWS_ID")
    AWS_SECRET_KEY = config("AWS_SECRET_KEY")

    # use the boto3 sdk to integrate python and aws s3
    client = boto3.client(
        "s3", aws_access_key_id=AWS_ID, aws_secret_access_key=AWS_SECRET_KEY
    )

    # get the object name and the object key(the actual .csv file)
    bucket_name = AWS_BUCKET_NAME
    # object_key = 'BTC_latest.csv'
    object_key = OBJECT_KEY

    csv_object = client.get_object(Bucket=bucket_name, Key=object_key)
    csv_body = csv_object["Body"]
    csv_string = csv_body.read().decode("utf-8")

    # load the dataset
    df = pd.read_csv(StringIO(csv_string))
    # get the date and closing price in order to forecast
    df_forecast = pd.DataFrame({"ds": [], "y": []})
    df_forecast["ds"], df_forecast["y"] = df["Date"], df["Close"]
    model_prop = Prophet(growth="linear", seasonality_mode="multiplicative")
    model_prop.fit(df_forecast)
    return model_prop


# prediction function
def predict(date=datetime.datetime.today(), model="bitcoin"):
    model_load = train(model="bitcoin")
    extra_days = FORECAST_INTERVAL
    # generate the forecast date_range dataframe
    end_date = date + datetime.timedelta(days=extra_days)
    date_frame = pd.date_range(start=date, end=end_date)
    dates = pd.DataFrame({"ds": date_frame})
    prediction = model_load.predict(dates)
    actual_pred = prediction[["ds", "trend"]]

    # visualize your trends to find  relevant insights
    model_load.plot(prediction).savefig(f"{model}_plot.png")
    model_load.plot_components(prediction).savefig(f"{model}_plot_components.png")
    return actual_pred.tail(extra_days).to_dict("records")
