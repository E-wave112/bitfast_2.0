from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from dateutil import parser
from datetime import datetime
import pandas as pd

URL = "https://coincodex.com/crypto/bitcoin/historical-data/"


def to_num(n):
    n_replace = n.replace("$", "")
    n_replace_dot = n_replace.replace(",", "")
    return float(n_replace_dot)


def to_time(x):
    x_parse = parser.parse(x)
    x_date = datetime.date(x_parse)
    return x_date


def get_btc_data():

    options = Options()
    firefox_browser = Firefox(options=options)
    firefox_browser.implicitly_wait(30)
    firefox_browser.get(URL)

    soup = firefox_browser.page_source
    df = pd.read_html(soup)[0]
    # get a list of the first seven closing prices in a list format
    df['Close'] = df['Close'].apply(lambda x: to_num(x))
    df['Date'] = df['Date'].apply(lambda n: to_time(n))
    df = df[['Date', 'Close']]
    new_df = df.tail(6)

    return new_df[::-1]
