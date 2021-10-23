from utils.get_data import get_btc_data
from random import randint
import s3fs
import tempfile
from decouple import config
import pandas as pd
import logging


AWS_KEY = config('AWS_ID')
AWS_SECRET = config('AWS_SECRET_KEY')

BUCKET_NAME = "edjangobucket"

# generate a random identifier to add to the db email field


def rand_identifier():
    rand_id = []
    for i in range(12):
        rand_id.append(chr(randint(65, 122)))

    return "".join(rand_id)


def get_s3fs():
    return s3fs.S3FileSystem(key=AWS_KEY, secret=AWS_SECRET)


def update_csv_file(file_name: str):
    
    with tempfile.TemporaryDirectory() as tmpdir:
        s3_fs = get_s3fs()
        s3_fs.get(f"{BUCKET_NAME}/{file_name}.csv", tmpdir + "/BTC_gotten.csv")

        # write to  and update the csv file with the latest bitcoin data
        with open(tmpdir + "/BTC_gotten.csv", "r+") as df:
            frame = pd.read_csv(df)
            new_frame = pd.concat([get_btc_data(), frame], ignore_index=True)
            # check the updated data
            print(new_frame.head(20))
            new_file = "BTC_updated"
            new_frame.to_csv(f"s3://{BUCKET_NAME}/{new_file}.csv", index=False)
            s3_bucket = f"s3://{BUCKET_NAME}/{new_file}.csv"
            logging.info(
                "This data has been updated in the bucket {}".format(s3_bucket))
    return "saved successfully"


print(update_csv_file("BTC_Data"))
