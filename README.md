# flask-ml
[![Python application](https://github.com/IDS-721-Final-Project/flask-ml/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/IDS-721-Final-Project/flask-ml/actions/workflows/python-app.yml)


# Introduction

This project puts a trained machine learning (ML) model into production environments. We adopt an trained model using Deep Evolution Strategy, which uses genetic algorithms to filter the neural network (such that backpropagation is not needed), and deploy it onto Google Cloud Kubernetes Engine. This creates a microservice-based application that ensures continuous availability.

## Architecture
![trade-robot-architecture](https://user-images.githubusercontent.com/37522943/116759840-5690d480-a9e1-11eb-8eda-f68b20789755.png)

This project contains two parts: 

1. ***flask-ml***: Dockerized backend functionality deployed on Kubernetes (grabs stock market info, does predictions using Deep Evolution Strategy etc.) 

2. ***trading_robot***: The place where users can specify the interested stock. Then the robot will automatically trade on it.

This repo is for the backend Kubernetes service part. How to use the trading robot is covered at the end.

# Usage

## 0. (Optional) Customize the Functionality

If you don't want to use the existing functionality and want to customize it, after your moodification, you can `make` before dockerizing it:

```
make
```
In the `Makefile`, it `install` new packages, does `pylint` and formatting using `black`. After running `Makefile` you can safely dockerize it in the following steps.


## 1. Build and Push Docker Container
First enter the `flask-ml` directory where the `Dockerfile` is stored. Also replace the `[PROJECT-ID]` with your project ID.

```bash
docker build -t ml-k8s .

docker tag ml-k8s gcr.io/[PROJECT-ID]/ml-k8s

docker push gcr.io/[PROJECT-ID]/ml-k8s
```

## 2. Deploy on Kubernetes

The overall structure of the project is as follows
```
| api.py
| base
  | namespace.yaml
  | deployment.yaml
  | service.yaml
  | kustomize.yaml
| Dockerfile
```

### 2.1 Setting up Kubernetes Clusters

Create a cluster called `k8s-ml-cluster`:
```bash
gcloud container clusters create k8s-ml-cluster --num-nodes 3 --machine-type g1-small --zone us-west1-b
```
Connect to the cluster `k8s-ml-cluster`:
```bash
gcloud container clusters get-credentials k8s-ml-cluster --zone us-west1-b --project [PROJECT_ID]
```

### 2.2 Install Kustomize


`Kustomize` is used to easily customize raw, template-free YAML files, without touching the hard-to-manage original YAML.
```bash
tar xzf ./kustomize_v4.1.2_linux_arm64.tar.gz

sudo mv kustomize /usr/bin/
```


### 2.3 Deploy the Pod


After setting up the YAML, we use the following command to deploy our app:
```bash
kubectl apply --kustomize=${PWD}/base/ --record=true
```
#### Optional:
See all components deployed into the namespace:
```bash
kubectl get ns
```
See the status of the deployment:
```bash
kubectl get deployment -n mlops
```

See the status of the service:
```bash
kubectl get service -n mlops
```


## 3. Test the Deployed Model

Test the model:

(Note: You can get `[EXTERNAL_IP_ADDRESS]` by using the previous command `kubectl get service -n mlops`)
```bash
curl http://[EXTERNAL_IP_ADDRESS]:5000/
```
 
 [>> Next: Do Predictions with trading_robot interface](https://github.com/IDS-721-Final-Project/trading_robot)
