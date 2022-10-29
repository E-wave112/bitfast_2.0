![example workflow](https://github.com/E-wave112/bitfast_2.0/actions/workflows/tests.yml/badge.svg)
![codecov](https://img.shields.io/codecov/c/gh/E-wave112/bitfast_2.0?token=JMXVER0IMD)

### A bitcoin USD exchange rate predictor built with [FastAPI](https://fastapi.tiangolo.com/) and [FaunaDB](https://fauna.com/) 

* The predictor is powered by a [time-series-forecasting](https://en.wikipedia.org/wiki/Time_series) Machine Learning Model.


* **DATA-SOURCE** : [coinmarketcap](https://coinmarketcap.com/currencies/bitcoin/historical-data/)


* The current real-time exchange rate data of Bitcoin in NGN and USD currencies are provided via the [Coinbase Api](https://developers.coinbase.com/docs/wallet/guides/price-data)

* Check out the live API via [this](https://bitfast.herokuapp.com/docs) or [that](https://bitfast.herokuapp.com/redoc) link

### Metrics 
- NB: these metrics improve over time as the model keeps learning from new data and hyperparameters are tweaked
```
MAPE=0.1580988278794064
MAE=4238.996757222961
RMSE=4585.15513690739
```

### Getting Started

To get started with the project, ensure you have setup and activated a virtual environment, guides on that [here](https://realpython.com/python-virtual-environments-a-primer/)

clone the repository via the command

```
$ git clone https://github.com/E-wave112/bitfast_2.0
```
install dependencies

```
$ python3 -m pip install -r requirements.txt
```

### Running the development Server

start the server by running the bash script below:
```
$ bash start.sh
```

Alternatively, you can start the server using the command below:
```
$ uvicorn application:app --reload
```

the server will be running on http://localhost:8000/docs



**Wanna check out my other machine learning projects and implementations?**  see them all [here](https://github.com/E-wave112/ml_proj1).
