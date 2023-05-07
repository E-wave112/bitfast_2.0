![example workflow](https://github.com/E-wave112/bitfast_2.0/actions/workflows/tests.yml/badge.svg)
![codecov](https://img.shields.io/codecov/c/gh/E-wave112/bitfast_2.0?token=JMXVER0IMD)

### A bitcoin USD exchange rate predictor built with [FastAPI](https://fastapi.tiangolo.com/) and [FaunaDB](https://fauna.com/) 

* The predictor is powered by a [time-series-forecasting](https://en.wikipedia.org/wiki/Time_series) Machine Learning Model.


* **DATA-SOURCE** : [coinmarketcap](https://coinmarketcap.com/currencies/bitcoin/historical-data/)


* The current real-time exchange rate data of Bitcoin in NGN and USD currencies are provided via the [Coinbase Api](https://developers.coinbase.com/docs/wallet/guides/price-data)

* Check out the live API via [this](https://bitfast.onrender.com/docs) or [that](https://bitfast.onrender.com/redoc) link

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

### Containerizing the API

#### Build the initial docker image
```
$ docker-compose up --build
```
#### Running the Dev Docker container

To run the application, use the following command:

```
$ docker-compose up
```
* The app will be running on http://127.0.0.1:8000
* Access the docker image for this project on the cloud [here](https://hub.docker.com/repository/docker/ewave112/fake_space_image)
* It is not recommended to use alpine based images for this project(or most of any other python projects) and here's [why](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker#-alpine-python-warning)

* A useful resource on how to push your docker image to [DockerHub](https://hub.docker.com)  can be found [here](https://ropenscilabs.github.io/r-docker-tutorial/04-Dockerhub.html)

### Running the Kubernetes cluster locally

* Ensure you have [minikube](https://minikube.sigs.k8s.io/docs/start/) installed on your machine

* Start the minikube cluster by running the command below:
```
$ minikube start
```
* To check the status of the cluster, run the command below:
```
$ minikube status
```

* Create a service discovery pattern for the application by running the command below:
```
$ kubectl apply -f k8s/services/service.yaml
```
* To deploy the application to the cluster, run the command below:
```
$ kubectl apply -f k8s/deployments/deployment.yaml
```
* To check the status of the pods, run the command below:
```
$ kubectl get pods
```
* To check the status of the services, run the command below:
```
$ kubectl get services
```
* To access the application, tunnel the service via the command below (we need to do this because our k8s service is of type `LoadBalancer`):
```
$ minikube tunnel
```
* Check the external IP (because you are running the cluster locally, your external IP address will be 127.0.0.1). More guides on that [here](https://minikube.sigs.k8s.io/docs/handbook/accessing/#example-of-loadbalancer)
```
$ kubectl get services bitfast-service
```
* Open the url below in your browser (ensure the external IP is not **pending** )
```
$ http://<external-ip>:9500
```
* To delete the application, run the command below:
```
$ kubectl delete -f k8s/deployments/deployment.yaml
```
* To stop the minikube cluster, run the command below:
```
$ minikube stop
```
* To deploy your cluster to the cloud, check out the guides from the official [kubernetes](https://kubernetes.io/docs/setup/production-environment/) docs



**Wanna check out my other machine learning projects and implementations?**  see them all [here](https://github.com/E-wave112/ml_proj1).
